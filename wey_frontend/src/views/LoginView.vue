<template lang="">
  <div class="max-w-7xl mx-auto grid grid-cols-2 gap-4">

    <div class="main-left">
      <div class="p-12 bg-white border border-gray-200 rounded-lg">
        <h1 class="mb-6 text-2xl">Login</h1>
        <p class="mb-6 text-gray-500">
          Hello this logins! Hello this logins! Hello this logins! Hello this logins!
          Hello this logins! Hello this logins! Hello this logins! Hello this logins!
          Hello this logins! Hello this logins! Hello this logins! Hello this logins!
        </p>
        <p class="font-bold">
          Dont have an account? <RouterLink :to="{'name': 'signup'}" class="underline">Click here</RouterLink> to created one!
        </p>
      </div>
    </div>

    <div class="main-Right">
      <div class="p-12 bg-white border border-gray-200 rounded-lg">

        <!-- การใช้ .prevent Modifier ใน v-on:submit.prevent จะยกเลิกการส่งฟอร์ม (form submission) 
        และไม่ให้เกิดการรีโหลดหน้าหรือเปลี่ยนหน้าเว็บเมื่อเกิดเหตุการณ์ submit บนฟอร์ม 
        และให้ Vue.js เรียกใช้ฟังก์ชัน submitForm ที่เราได้กำหนดไว้เพื่อประมวลผลการส่งฟอร์มตามต้องการในที่นี้ -->
        <form class="space-y-6" v-on:submit.prevent="submitForm">
          
          <div class="space-y-6">
            <lable>E-mail</lable><br>
            <input type="Email" v-model="form.email" placeholder="Your email address" class="w-full mt-2 py-4 px-6 border-gray-200 rounded-lg">
          </div>

          <div class="space-y-6">
            <lable>Password</lable><br>
            <input type="password" v-model="form.password" placeholder="Your Password" class="w-full mt-2 py-4 px-6 border-gray-200 rounded-lg">
          </div>


          <template v-if="errors.length > 0">
            <div class="bg-red-300 text-white rounded-lg p-6">
              <p v-for="error in errors" v-bind:key="error">{{ error }}</p>
            </div>
          </template>

          <div>
            <button class="py-4 px-6 bg-yellow-400 text-white rounded-lg">Login</button>
          </div>
        </form>
      </div>
    </div>

  </div>
</template>


<script>
import axios from 'axios'
import { useUserStore } from '@/stores/user'


export default {

  setup(){
    const userStore = useUserStore()

    return {
      userStore
    }
  },
  data() {
    return {
      form: {
        email: '',
        password: '',
      },
      errors: [],
    }
  },
  
  methods: {
    async submitForm() {

      this.errors = []
      
      if(this.form.email === ''){
        this.errors.push('Your email is missing')

      }
      if(this.form.password === ''){
        this.errors.push('Your password is missing')

      }

      if(this.errors.length === 0){

        // ใช้หน้า login ยืนยันตัวตน  
        await axios
          .post('/api/login/', this.form)
          .then(response => {
            this.userStore.setToken(response.data)

            console.log(response.data.access)

            axios.defaults.headers.common["Authorization"] = "Bearer " + response.data.access


          })
          .catch(error => {
            console.log('error', error)
          })
        // ใช้หน้า login ส่งข้อมูลไปที่หน้า feed  
        await axios
          .get('/api/me/')
          .then(response => {
            this.userStore.setUserInfo(response.data)

            this.$router.push('/feed')

          })
          .catch(error => {
            console.log('error', error)
          })

      }

    }
  }
  
}
</script>
<style lang="">
  
</style>
