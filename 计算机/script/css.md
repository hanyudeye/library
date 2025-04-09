---
layout: default
toc: false
title: css
date:  2025-01-22T15:47:48+08:00
---

 
## CSS 排版与网格布局教程

CSS 排版与网格布局是现代前端开发中非常重要的技能。它们能帮助我们创建灵活且响应式的布局。以下是一个详细的 CSS 排版与网格布局教程，涵盖了基础和进阶概念。

### 1. **CSS 排版基础**
CSS 排版主要涉及如何控制文字的排列、行高、间距、对齐等。了解这些基础是构建网页时的第一步。

#### 1.1 **字体设置**
```css
body {
    font-family: Arial, sans-serif; /* 设置字体 */
    font-size: 16px; /* 字体大小 */
    line-height: 1.5; /* 行高 */
    color: #333; /* 文字颜色 */
    text-align: justify; /* 设置文字两端对齐 */
}
```
- `font-family`：设置字体系列。
- `font-size`：设置字体大小。
- `line-height`：设置行高，使文字行间距适合阅读。
- `text-align`：控制文本对齐方式（左对齐、右对齐、居中或两端对齐）。

#### 1.2 **文本装饰**
```css
h1 {
    text-decoration: underline; /* 下划线 */
    text-transform: uppercase; /* 转换为大写 */
}
```
- `text-decoration`：为文本添加装饰（如下划线、删除线等）。
- `text-transform`：设置文本大小写（如大写、小写、首字母大写等）。

#### 1.3 **文字间距和行间距**
```css
p {
    letter-spacing: 0.1em; /* 字母间距 */
    word-spacing: 0.3em; /* 单词间距 */
}
```
- `letter-spacing`：控制字符之间的距离。
- `word-spacing`：控制单词之间的距离。

#### 1.4 **多列布局**
```css
.container {
    column-count: 3; /* 分成3列 */
    column-gap: 20px; /* 列之间的间距 */
}
```
- `column-count`：设置列的数量。
- `column-gap`：设置列之间的间距。

---

### 2. **CSS 网格布局 (CSS Grid)**
CSS Grid 是一种强大的布局系统，它可以让我们创建更加灵活和响应式的网页布局。

#### 2.1 **基本的网格布局**
```css
.container {
    display: grid;
    grid-template-columns: repeat(3, 1fr); /* 创建3列，每列占1fr的空间 */
    gap: 20px; /* 列与列之间的间隙 */
}
.item {
    background-color: #f4f4f4;
    padding: 20px;
}
```
- `display: grid`：启用网格布局。
- `grid-template-columns`：定义列的宽度，这里使用 `repeat(3, 1fr)` 创建3列，每列占1份可用空间。
- `gap`：列与列之间的间隙。

#### 2.2 **定义网格行和列**
```css
.container {
    display: grid;
    grid-template-columns: 1fr 2fr 1fr; /* 三列宽度比例 */
    grid-template-rows: 100px auto; /* 第一行固定100px，高度自适应 */
    gap: 20px;
}
```
- `grid-template-columns`：定义列的宽度，可以使用 `fr`（分配可用空间的单位）来定义比例。
- `grid-template-rows`：定义行的高度。

#### 2.3 **使用 `grid-template-areas` 定义网格布局**
```css
.container {
    display: grid;
    grid-template-columns: 1fr 2fr;
    grid-template-rows: 100px auto;
    grid-template-areas:
        "header header"
        "sidebar main"
        "footer footer";
    gap: 20px;
}

.header {
    grid-area: header;
}
.sidebar {
    grid-area: sidebar;
}
.main {
    grid-area: main;
}
.footer {
    grid-area: footer;
}
```
- `grid-template-areas`：为网格区域命名，这样可以更加直观地定义布局。
- `grid-area`：指定元素放置在命名的区域中。

#### 2.4 **网格项目的对齐**
```css
.container {
    display: grid;
    grid-template-columns: 1fr 2fr 1fr;
    gap: 20px;
    align-items: center; /* 垂直居中 */
    justify-items: center; /* 水平居中 */
}
```
- `align-items`：控制网格项目在行方向上的对齐（垂直对齐）。
- `justify-items`：控制网格项目在列方向上的对齐（水平方向对齐）。

#### 2.5 **网格容器的对齐**
```css
.container {
    display: grid;
    grid-template-columns: 1fr 2fr 1fr;
    gap: 20px;
    align-content: center; /* 垂直对齐容器内容 */
    justify-content: center; /* 水平对齐容器内容 */
}
```
- `align-content`：控制整个网格容器在行方向上的对齐。
- `justify-content`：控制整个网格容器在列方向上的对齐。

---

### 3. **响应式网格布局**
为了确保网页在不同设备上都能正确显示，响应式设计是非常重要的。我们可以使用 `@media` 查询来调整网格布局。

#### 3.1 **使用 `@media` 进行响应式设计**
```css
.container {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 20px;
}

@media (max-width: 768px) {
    .container {
        grid-template-columns: 1fr; /* 当屏幕宽度小于768px时，显示为单列 */
    }
}
```
- `@media` 查询：根据屏幕尺寸调整布局。这里，当屏幕宽度小于 768px 时，网格布局从 3 列变为 1 列。

#### 3.2 **使用 `fr` 和百分比单位进行灵活布局**
```css
.container {
    display: grid;
    grid-template-columns: 1fr 3fr; /* 1:3比例 */
    gap: 20px;
}

@media (max-width: 600px) {
    .container {
        grid-template-columns: 1fr; /* 小屏幕下单列布局 */
    }
}
```
- `1fr` 和 `3fr`：表示 1 份和 3 份的可用空间。这样可以创建灵活的比例布局。
  
---

### 4. **CSS Flexbox 与 Grid 配合使用**
在某些复杂布局中，Flexbox 和 Grid 可以组合使用。

```css
.container {
    display: grid;
    grid-template-columns: 1fr 3fr;
    gap: 20px;
}

.sidebar {
    display: flex; /* 使用 Flexbox 来布局侧边栏 */
    flex-direction: column; /* 垂直布局 */
    gap: 10px;
}
```
- **Grid** 用于大体布局（如主内容区和侧边栏），**Flexbox** 用于细节布局（如侧边栏中的项目排列）。

---

### 总结
- **CSS 排版**：理解文本、字体和布局控制是构建网页的基础，涉及文本对齐、行高、字母间距等内容。
- **CSS Grid**：强大的布局工具，可以创建多列多行的复杂布局，且支持命名区域和响应式设计。
- **响应式设计**：结合 `@media` 查询，根据不同设备屏幕尺寸调整布局，确保网站在各种设备上表现良好。

通过学习这些基础和进阶的 CSS 排版技巧，你可以轻松地设计并实现现代网页布局。

## 拖拽
``` html
    <!--给 box1 增加拖拽的属性-->
    <div class="box1" draggable="true"></div>
 ```