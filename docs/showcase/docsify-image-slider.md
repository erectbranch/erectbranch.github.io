<div align="center">

# docsify-image-slider

[![GitHub Release](https://img.shields.io/github/v/release/erectbranch/docsify-image-slider?logo=github&color=orange&style=flat-square)](https://github.com/erectbranch/docsify-image-slider/releases)
[![NPM Release](https://img.shields.io/npm/v/docsify-image-slider.svg?logo=npm&style=flat-square)](https://www.npmjs.com/package/docsify-image-slider)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=flat-square)](https://github.com/erectbranch/docsify-image-slider/blob/master/LICENSE)

A plugin for [Docsify](https://docsify.js.org/#/) that allows you to create a slider for images in your documentation.

</div>

## 🔨 Import

To use the image slider, you need to include the plugin in your Docsify `index.html` file:

**Add stylesheet**

```html
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/docsify-image-slider/dist/slider.min.css">
```

**Add script**

```html
<script src="//cdn.jsdelivr.net/npm/docsify-image-slider/dist/docsify-image-slider.min.js"></script>
```

---

## 💡 Demo

<div class="image-slider">
    [[slider]](./images/slide_1.jpg|./images/slide_2.jpg|./images/slide_3.jpg)
</div>

---

## 📋 Usage

1. Define a `<div class="image-slider"> </div>` wrapper for the slider.

    ```markdown
    <div class="image-slider">
        ...
    </div>
    ```

2. Inside the wrapper, use the `[[slider]]` syntax followed by the image URLs separated by a pipe (`|`). The URLs can be relative or absolute.

    **Syntax**: \[\[**slider**\]\]**(img url 1|img url 2|img url 3)**

    ```markdown
    <div class="image-slider">
        Syntax
    </div>
    ```

---

## ⚙️ Configuration

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

---

## 🎨 Customization

The slider can be customized using CSS. You can override the following CSS variables.

| Style | Description |
| --- | --- |
| `--docsify-image-slider-transition` | Transition effect for the slider. |
| `--docsify-image-slider-width` | Width of the slide. |
| `--docsify-image-slider-height` | Height of the slide. |
| `--docsify-image-slider-max-width` | Maximum width of the slide. |
| `--docsify-image-slider-overflow` | Overflow property for the slide. |
| `--docsify-image-slider-button-color` | Color of the slider arrows. |
| `--docsify-image-slider-button-bg-color` | Background color of the slider buttons. |
| `--docsify-image-slider-button-border-color` | Border color of the slider buttons. |

To change the transition effect and the size of the slider, you can add the following styles to your `index.html` file:

```html
<style>
  :root {
    /* slider-buttons */
    --docsify-image-slider-button-color: #000000;
    --docsify-image-slider-button-border-color: #000000;
  }
</style>
```

---

## ✨ Contribution

Please feel free to submit a pull request or open an issue on the GitHub repository. Your contributions are welcome and appreciated!

---