import {defineConfig} from 'vitepress'
import AutoNav from "vite-plugin-vitepress-auto-nav";//https://xaviw.github.io/XaviDocs/%E5%B7%A5%E5%85%B7%E7%B3%BB%E5%88%97/VitePress%E6%90%AD%E5%BB%BA/%E8%87%AA%E5%8A%A8%E7%94%9F%E6%88%90%E7%9B%AE%E5%BD%95.html
export default defineConfig({
    title: "九问Blog",
    description: "欢迎访问九问Blog！分享一些Python全栈开发以及爬虫技术，希望对你有所帮助",
    srcDir: 'docs',
    themeConfig: {
        socialLinks: [
            {icon: 'github', link: 'https://github.com/jiuwen567'},
            {
                icon: {
                    svg: '<svg t="1724307958358" class="icon" viewBox="0 0 1024 1024" version="1.1" xmlns="http://www.w3.org/2000/svg" p-id="4234" width="200" height="200"><path d="M512 0C230.4 0 0 230.4 0 512s230.4 512 512 512 512-230.4 512-512S793.6 0 512 0z m284.8 313.6c0 12.8-12.8 25.6-25.6 25.6H416c-41.6 0-76.8 35.2-76.8 76.8v243.2c0 12.8 12.8 25.6 25.6 25.6h240c41.6 0 76.8-35.2 76.8-76.8v-12.8c0-12.8-12.8-25.6-25.6-25.6H480c-12.8 0-25.6-12.8-25.6-25.6v-64c0-12.8 12.8-25.6 25.6-25.6h291.2c12.8 0 25.6 12.8 25.6 25.6v144c0 92.8-76.8 169.6-169.6 169.6H252.8c-12.8 0-25.6-12.8-25.6-25.6V412.8C227.2 310.4 310.4 224 416 224h355.2c12.8 0 25.6 12.8 25.6 25.6v64z" fill="#B32225" p-id="4235"></path></svg>'
                }, link: "https://gitee.com/jiuwen567",
            }
        ],
        footer: {
            message: 'Released under the MIT License.',
            copyright: 'Copyright © 2024.8.15-present 九问.All Rights Reserved.'
        },
        search: {
            provider: 'local'
        },
        // editLink: {
        //     pattern: 'https://github.com/vuejs/vitepress/edit/main/docs/:path',
        //     text: 'Edit this page on GitHub'
        // }
    },
    vite: {
        plugins: [
            AutoNav({
                // 自定义配置
                compareFn: (b, a) => {
                    // 按最新提交时间(没有提交记录时为本地文件修改时间)升序排列
                    return (b.options.lastCommitTime || b.options.modifyTime) - (a.options.lastCommitTime || a.options.modifyTime)
                },
                // useArticleTitle: true // 全局开启使用文章一级标题作为文章名称
            }),
        ],
    },
    markdown: {
        math: true
    },
})