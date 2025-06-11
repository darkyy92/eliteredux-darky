import { defineConfig } from 'vitepress'
import { readdirSync } from 'fs'
import { join, basename } from 'path'
import { fileURLToPath } from 'url'

const __dirname = fileURLToPath(new URL('.', import.meta.url))

// Function to get all ability files - reads from both locations
function getAbilityFiles() {
  // Try docs/abilities first (copied files)
  let abilitiesDir = join(__dirname, '../abilities')
  let files = []
  
  try {
    files = readdirSync(abilitiesDir)
      .filter(file => file.endsWith('.md') && file !== 'index.md')
  } catch {
    // If that fails, try reading from knowledge/abilities
    try {
      abilitiesDir = join(__dirname, '../../../knowledge/abilities')
      files = readdirSync(abilitiesDir)
        .filter(file => file.endsWith('.md') && file !== 'index.md' && file !== 'README.md')
    } catch {
      console.warn('No ability files found in either location')
      return []
    }
  }
  
  // Sort files numerically by the ID prefix
  files.sort((a, b) => {
    const numA = parseInt(a.split('_')[0])
    const numB = parseInt(b.split('_')[0])
    return numA - numB
  })
  
  return files.map(file => {
    const nameWithoutExt = file.replace('.md', '')
    const [id, ...nameParts] = nameWithoutExt.split('_')
    
    // Title case each word in the ability name
    const formattedName = nameParts
      .join(' ')
      .replace(/\b\w/g, char => char.toUpperCase())
    
    const displayText = `${id} ${formattedName}`
    
    return {
      text: displayText,
      link: `/abilities/${nameWithoutExt}`
    }
  })
}

export default defineConfig({
  title: 'Elite Redux Ability Codex',
  description: 'Comprehensive documentation of all Elite Redux abilities',
  
  // Base URL for custom domain
  base: '/',
  
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
  srcDir: '.'
})