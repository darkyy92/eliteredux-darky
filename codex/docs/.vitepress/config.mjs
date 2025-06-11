import { defineConfig } from 'vitepress'
import { readdirSync } from 'fs'
import { join, basename } from 'path'
import { fileURLToPath } from 'url'

const __dirname = fileURLToPath(new URL('.', import.meta.url))

// Function to get all ability files
function getAbilityFiles() {
  const abilitiesDir = join(__dirname, '../../../knowledge/abilities')
  try {
    const files = readdirSync(abilitiesDir)
      .filter(file => file.endsWith('.md'))
      .sort()
    
    return files.map(file => ({
      text: file.replace('.md', '').replace(/_/g, ' '),
      link: `/abilities/${file.replace('.md', '')}`
    }))
  } catch {
    return []
  }
}

export default defineConfig({
  title: 'Elite Redux Ability Codex',
  description: 'Comprehensive documentation of all Elite Redux abilities',
  
  // Base URL for GitHub Pages - will be updated when we know the repo name
  base: '/eliteredux-darky/',
  
  // Dark theme by default
  appearance: 'dark',
  
  // Theme configuration
  themeConfig: {
    // Enable search
    search: {
      provider: 'local',
      options: {
        placeholder: 'Search abilities...',
        detailedView: true
      }
    },
    
    // Navigation
    nav: [
      { text: 'Home', link: '/' },
      { text: 'Abilities', link: '/abilities/' }
    ],
    
    // Sidebar with all abilities
    sidebar: {
      '/abilities/': [
        {
          text: 'All Abilities',
          collapsed: false,
          items: getAbilityFiles()
        }
      ]
    },
    
    // Social links
    socialLinks: [
      { icon: 'github', link: 'https://github.com/darkyy92/eliteredux-darky' }
    ],
    
    // Footer
    footer: {
      message: 'Elite Redux Ability Codex',
      copyright: 'Elite Redux Development Team'
    }
  },
  
  // Markdown configuration
  markdown: {
    theme: {
      light: 'github-dark',
      dark: 'github-dark'
    }
  },
  
  // Source directory configuration
  srcDir: '.',
  
  // Rewrites to map knowledge/abilities to /abilities route
  rewrites: {
    '../../knowledge/abilities/:file.md': 'abilities/:file.md'
  }
})