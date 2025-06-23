import { defineConfig } from 'vitepress'
import { readdirSync, readFileSync } from 'fs'
import { join, basename } from 'path'
import { fileURLToPath } from 'url'
import matter from 'gray-matter'

const __dirname = fileURLToPath(new URL('.', import.meta.url))

// Function to get all ability files with frontmatter data
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
    
    // Read file to check frontmatter
    let isReviewed = false
    try {
      const filePath = join(abilitiesDir, file)
      const content = readFileSync(filePath, 'utf-8')
      const { data } = matter(content)
      isReviewed = data.status === 'reviewed'
    } catch (e) {
      // If can't read frontmatter, assume not reviewed
    }
    
    // Title case each word in the ability name
    const formattedName = nameParts
      .join(' ')
      .replace(/\b\w/g, char => char.toUpperCase())
    
    // Add checkmark if reviewed
    const displayText = isReviewed 
      ? `✅ ${id} ${formattedName}`
      : `${id} ${formattedName}`
    
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
  
  // Head configuration for favicon
  head: [
    ['link', { rel: 'icon', type: 'image/svg+xml', href: '/favicon.svg' }],
    ['link', { rel: 'icon', type: 'image/png', sizes: '32x32', href: '/favicon-32x32.png' }],
    ['link', { rel: 'icon', type: 'image/png', sizes: '16x16', href: '/favicon-16x16.png' }],
    ['link', { rel: 'apple-touch-icon', sizes: '180x180', href: '/apple-touch-icon.png' }],
    ['meta', { name: 'theme-color', content: '#4f46e5' }]
  ],
  
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
      { text: 'Abilities', link: '/abilities/' },
      { text: 'Contributing', link: '/contributing' },
      { text: 'Discord', link: 'http://discord.elite-redux.com' },
      { text: 'Pokédex', link: 'http://dex.elite-redux.com' },
      { text: 'Wiki', link: 'https://wiki.elite-redux.com' }
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
    socialLinks: [],
    
    // Footer
    footer: {
      message: 'Elite Redux Ability Codex',
      copyright: 'Elite Redux Development Team'
    }
  },
  
  // Markdown configuration
  markdown: {
    theme: {
      light: 'github-light',
      dark: 'github-dark'
    }
  },
  
  // Source directory configuration
  srcDir: '.'
})