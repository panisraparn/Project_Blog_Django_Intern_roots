<template>
  <p><strong>Mian Menu Component-emits</strong></p>
  <h6>Enter Your Name!</h6>
  <!-- <button @click="$emit('closeMenu')">Close Menu</button> -->
  <!-- <button @click="$emit('closeMenu', 'John Doe')">Close Menu</button> -->
  <p><input type="text" v-model="name" class="p-4 w-full bg-gray-100 rounded-lg"></p>
  <button @click="$emit('closeMenu', name)" class="inline-block py-4 px-6 bg-yellow-800 text-white rounded-lg">Close Menu</button>

</template>

<script>
export default {
  // emits: ['closeMenu'],
  emits: {
    closeMenu(name) {
      if(!name)
        return false;
      else
        return true;
    }
  },
  data(){
    return { name: ''}
  }
}
</script>
