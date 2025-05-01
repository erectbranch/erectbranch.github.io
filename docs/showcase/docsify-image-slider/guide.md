<div align="center">

# docsify-image-slider

[![GitHub Release](https://img.shields.io/github/v/release/erectbranch/docsify-image-slider?logo=github&color=orange&style=flat-square)](https://github.com/erectbranch/docsify-image-slider/releases)
[![NPM Release](https://img.shields.io/npm/v/docsify-image-slider.svg?logo=npm&style=flat-square)](https://www.npmjs.com/package/docsify-image-slider)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=flat-square)](https://github.com/erectbranch/docsify-image-slider/blob/master/LICENSE)

A plugin for [Docsify](https://docsify.js.org/#/) that allows you to create a slider for images in your documentation.

</div>

## 1. Import

To use the image slider, you need to include the plugin in your Docsify `index.html` file:

**Add stylesheet**

```html
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/docsify-image-slider@latest/dist/slider.min.css">
```

**Add script**

```html
<script src="//cdn.jsdelivr.net/npm/docsify-image-slider@latest/dist/docsify-image-slider.min.js"></script>
```

## 2. Demo

[[slider]](./images/slide_1.jpg|./images/slide_2.jpg|./images/slide_3.jpg)

## 3. Usage

> \[\[**slider**\]\]**(img url 1|img url 2|...|img url n)**

## Configuration

To configure the slider, you can set options in your `index.html` file. The available options are:

| Option | Type | Default | Description |
| --- | --- | --- | --- |
| `auto` | `Boolean` | false | Whether to automatically switch images. |
| `intervalTime` | `Int` | 20000 | Time interval for automatic switching (in milliseconds). |

```javascript
window.$docsify = {
  slider: {
    // Default options
    auto: false,
    intervalTime: 20000,
  },
};
```

## 4. Customization

The slider can be customized using CSS. You can override the following CSS variables.

| Style | Description |
| --- | --- |
| `--docsify-image-slider-transition` | Transition effect for the slider. |
| `--docsify-image-slider-width` | Width of the slide. |
| `--docsify-image-slider-height` | Height of the slide. |
| `--docsify-image-slider-max-width` | Maximum width of the slide. |
| `--docsify-image-slider-overflow` | Overflow property for the slide. |
| `--docsify-image-slider-left-right-margin` | Margin for the left and right sides of the slider buttons. |
| `--docsify-image-slider-button-color` | Color of the slider arrows. |
| `--docsify-image-slider-button-bg-color` | Background color of the slider buttons. |
| `--docsify-image-slider-button-bg-hover-color` | Background color of the slider buttons on hover. |
| `--docsify-image-slider-button-border-color` | Border color of the slider buttons. |

To change the transition effect and the size of the slider, you can add the following styles to your `index.html` file:

```html
<style>
  :root {
    /* slider */
    --docsify-image-slider-transition: 0.4s ease-in-out;
    --docsify-image-slider-width: 50vw;
    --docsify-image-slider-height: 50vh;
    --docsify-image-slider-max-width: 768px;
    --docsify-image-slider-overflow: hidden;
    --docsify-image-slider-left-right-margin: -3rem;

    /* slider-buttons */
    --docsify-image-slider-button-color: #a0a0a0;
    --docsify-image-slider-button-bg-color: transparent;
    --docsify-image-slider-button-bg-hover-color: #a0a0a01A;
    --docsify-image-slider-button-border-color: #a0a0a0;
  }
</style>
```

## 5. Contribution

Your contributions are welcome and appreciated!
