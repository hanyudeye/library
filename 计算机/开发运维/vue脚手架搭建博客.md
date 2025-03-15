 使用 Vue CLI 脚手架搭建一个简单的个人博客，包括博客功能列表页面、内容页面和导航菜单，可以按照以下步骤进行：

### 步骤 1：安装 Vue CLI

如果你还没有安装 Vue CLI，请先安装它。在命令行中运行以下命令：

```bash
npm install -g @vue/cli
```

### 步骤 2：创建 Vue 项目

在命令行中，使用 Vue CLI 创建一个新项目：

```bash
vue create personal-blog
```

根据提示选择默认设置，或者自定义配置。

### 步骤 3：安装依赖（可选）

如果需要使用 Vue Router 和其他库，可以在项目创建完成后进入项目目录并安装依赖：

```bash
cd personal-blog
vue add router
```

选择“是”以启用历史模式（HTML5 History Mode）。

### 步骤 4：项目结构

项目创建完成后，进入 `src` 目录，您将看到以下结构：

```
src
├── assets
├── components
├── router
│   └── index.js
├── views
├── App.vue
└── main.js
```

### 步骤 5：创建博客功能列表页面

1. **创建 `BlogList.vue` 组件**：
   在 `src/views` 目录下创建 `BlogList.vue` 文件，并添加以下代码：

   ```vue
   <template>
     <div>
       <h1>博客列表</h1>
       <ul>
         <li v-for="post in posts" :key="post.id">
           <router-link :to="{ name: 'BlogDetail', params: { id: post.id } }">
             {{ post.title }}
           </router-link>
         </li>
       </ul>
     </div>
   </template>

   <script>
   export default {
     data() {
       return {
         posts: [
           { id: 1, title: '第一篇博客' },
           { id: 2, title: '第二篇博客' },
           { id: 3, title: '第三篇博客' },
         ],
       };
     },
   };
   </script>

   <style scoped>
   /* 自定义样式 */
   </style>
   ```

2. **创建 `BlogDetail.vue` 组件**：
   在 `src/views` 目录下创建 `BlogDetail.vue` 文件，并添加以下代码：

   ```vue
   <template>
     <div>
       <h1>{{ post.title }}</h1>
       <p>{{ post.content }}</p>
     </div>
   </template>

   <script>
   export default {
     data() {
       return {
         post: {},
       };
     },
     mounted() {
       const id = this.$route.params.id;
       // 模拟从服务器获取数据
       const posts = [
         { id: 1, title: '第一篇博客', content: '这是第一篇博客内容。' },
         { id: 2, title: '第二篇博客', content: '这是第二篇博客内容。' },
         { id: 3, title: '第三篇博客', content: '这是第三篇博客内容。' },
       ];
       this.post = posts.find(post => post.id === parseInt(id));
     },
   };
   </script>

   <style scoped>
   /* 自定义样式 */
   </style>
   ```

### 步骤 6：设置路由

在 `src/router/index.js` 中，添加博客列表和内容页面的路由：

```javascript
import Vue from 'vue';
import Router from 'vue-router';
import BlogList from '../views/BlogList.vue';
import BlogDetail from '../views/BlogDetail.vue';

Vue.use(Router);

const routes = [
  {
    path: '/',
    name: 'BlogList',
    component: BlogList,
  },
  {
    path: '/blog/:id',
    name: 'BlogDetail',
    component: BlogDetail,
  },
];

const router = new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes,
});

export default router;
```

### 步骤 7：添加导航菜单

在 `src/App.vue` 文件中，添加导航菜单：

```vue
<template>
  <div id="app">
    <nav>
      <router-link to="/">博客列表</router-link>
    </nav>
    <router-view />
  </div>
</template>

<script>
export default {
  name: 'App',
};
</script>

<style>
nav {
  padding: 10px;
  background: #f3f3f3;
}
nav a {
  margin: 0 10px;
  text-decoration: none;
}
</style>
```

### 步骤 8：运行项目

完成上述步骤后，您可以在命令行中运行以下命令以启动项目：

```bash
npm run serve
```

### 访问您的博客

打开浏览器并访问 `http://localhost:8080`，您应该能看到博客列表页面。点击每篇博客标题可以进入内容页面。

### 总结

通过以上步骤，您已经搭建了一个简单的个人博客，包含博客列表页面、内容页面和导航菜单。您可以继续扩展功能，如添加样式、增加评论功能、集成 API 等。