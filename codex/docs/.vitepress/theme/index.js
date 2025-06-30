import DefaultTheme from 'vitepress/theme'
import { h } from 'vue'
import './custom.css'
import InlineAbilityEditor from './components/InlineAbilityEditor.vue'
import SidebarAutoScroll from './components/SidebarAutoScroll.vue'

export default {
  extends: DefaultTheme,
  enhanceApp({ app }) {
    // Register global components
    app.component('InlineAbilityEditor', InlineAbilityEditor)
    app.component('SidebarAutoScroll', SidebarAutoScroll)
  },
  Layout() {
    return h(DefaultTheme.Layout, null, {
      'doc-before': () => h(InlineAbilityEditor),
      'layout-bottom': () => h(SidebarAutoScroll)
    })
  }
}