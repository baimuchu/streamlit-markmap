import streamlit as st
from streamlit_markmap import markmap

st.set_page_config(page_title="markmap", layout="wide")



st.write('## example1')
with open('markdown_data/data.md', encoding='utf-8') as fp:
    md = fp.read()

markmap(md,height=400)

st.write('## example2')
data = '''
---
title: markmap
markmap:
  maxWidth: 200
  colorFreezeLevel: 2
  initialExpandLevel: 4
---

## Links

- [Website](https://markmap.js.org/)
- [GitHub](https://github.com/gera2ld/markmap)

## Related Projects

- [coc-markmap](https://github.com/gera2ld/coc-markmap) for Neovim
- [markmap-vscode](https://marketplace.visualstudio.com/items?itemName=gera2ld.markmap-vscode) for VSCode
- [eaf-markmap](https://github.com/emacs-eaf/eaf-markmap) for Emacs

## Features

Note that if blocks and lists appear at the same level, the lists will be ignored.

### Lists

- **strong** ~~del~~ *italic* ==highlight==
- `inline code`
- Katex: $x = {-b \pm \sqrt{b^2-4ac} \over 2a}$ <!-- markmap: fold -->
  - [More Katex Examples](#?d=gist:af76a4c245b302206b16aec503dbe07b:katex.md)
- Now we can wrap very very very very long text based on `maxWidth` option or `<br>` tag.
- Ordered list
  1. item 1
  2. item 2

### Blocks

```js
console.log('hello, JavaScript')
```

| Products | Price |
|-|-|
| Apple | 4 |
| Banana | 2 |

![](/favicon.png)
'''

markmap(data, height=400)



