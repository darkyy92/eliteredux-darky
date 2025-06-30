<template>
  <!-- This component doesn't render anything visible -->
  <div></div>
</template>

<script setup>
import { watch, nextTick, onMounted } from 'vue'
import { useRoute } from 'vitepress'

const route = useRoute()

// Function to scroll sidebar to active item
async function scrollToActiveItem() {
  // Wait for DOM updates
  await nextTick()
  
  // Only run on desktop (sidebar hidden on mobile)
  if (window.innerWidth <= 768) return
  
  // Small delay to ensure VitePress has updated the active state
  setTimeout(() => {
    // Find the active sidebar item
    const activeItem = document.querySelector('.VPSidebarItem.is-active')
    if (!activeItem) return
    
    // Find the sidebar container
    const sidebar = document.querySelector('.VPSidebar .content')
    if (!sidebar) return
    
    // Calculate position to center the active item
    const itemRect = activeItem.getBoundingClientRect()
    const sidebarRect = sidebar.getBoundingClientRect()
    
    // Calculate the scroll position to center the item
    const scrollTop = activeItem.offsetTop - (sidebarRect.height / 2) + (itemRect.height / 2)
    
    // Smooth scroll to the active item
    sidebar.scrollTo({
      top: scrollTop,
      behavior: 'smooth'
    })
  }, 100) // Small delay to ensure DOM is ready
}

// Watch for route changes
watch(() => route.path, async () => {
  await scrollToActiveItem()
})

// Also scroll on initial mount
onMounted(async () => {
  await scrollToActiveItem()
})

// Listen for window resize to handle responsive changes
let resizeTimeout
window.addEventListener('resize', () => {
  clearTimeout(resizeTimeout)
  resizeTimeout = setTimeout(scrollToActiveItem, 200)
})
</script>

<style scoped>
/* No styles needed for this utility component */
</style>