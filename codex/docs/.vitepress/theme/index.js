import DefaultTheme from 'vitepress/theme'
import { h } from 'vue'
import './custom.css'
import InlineAbilityEditor from './components/InlineAbilityEditor.vue'

export default {
  extends: DefaultTheme,
  enhanceApp({ app }) {
    // Register global components
    app.component('InlineAbilityEditor', InlineAbilityEditor)
  },
  Layout() {
    return h(DefaultTheme.Layout, null, {
      'doc-before': () => h(InlineAbilityEditor)
    })
  }
}