<template>
  <div class="p-4 bg-white border border-gray-200 text-center rounded-lg">
    <p>props</p>
    <!-- <p>This is greeting, {{ greeting }}</p> -->
    <!-- <p>Hello- {{firstName}}-{{ lastName}}</p> -->
    <p>Hello- {{fullName}} </p>
    
  </div>
</template>
<script>

export default {
  //prop pass data from parent component , down to child component
  
  //aray props
  // props: ['greeting']
  //props: ['fullName']

  //object props
  // props: {
  //   fullName: String
  // }

  //required props
  props: {
    fullName: {
      type: String,
      // required: true
      default: 'Unknow',
    }
  }

  
}
</script>
