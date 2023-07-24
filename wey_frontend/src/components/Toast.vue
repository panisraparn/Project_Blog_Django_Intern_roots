<script setup>
// ดึง useToastStore จาก folder store
import { useToastStore } from '@/stores/toast'  
const store = useToastStore()

// return {
//   store
// }
</script>
<template>
  <div v-if="store.isVisible" 
  class="transition ease-in-out daley-500 px-6 py-6 fixed top-full right-8 rounded-xl shadow-xl" 
  :class="store.classes">

  {{ store.message }}

  </div>
</template>
