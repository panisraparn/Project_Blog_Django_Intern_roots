<template>
  
  <!-- props -->
  <!-- <child-greeting greeting='Hello' /> -->
  <!-- <child-greeting first-name="John" last-name="Doe" /> -->
  <!-- <child-greeting :first-name="fName" :last-name="lName" /> -->
  <!-- <child-greeting :full-name="fullName" /> -->
  <child-greeting  />



  <p><strong> {{item.id}}-{{ item.name }}  </strong></p>
  
<div class="p-4 bg-white border border-gray-200 text-center rounded-lg">
  <Form @submit="onSubmit">
    <div class="mb-4">
      <Field  
        class="border border-gray-300" 
        name="saySomething"
        v-model="sayText" 
        type="textarea" 
        placeholder="say something!" 
        :rules="validateEmail"
      />
      <ErrorMessage name="saySomething" />
    </div>
    <button class="inline-block py-4 px-6 bg-yellow-800 text-white rounded-lg">Sign up for newsletter</button>
  </Form>

          <!-- <Form v-on:submit.prevent="updateTopicForm" method="put">
          <div class="p-4">
            <Field 
            
            type="textarea" 
            v-model="updatedName" 
            class="p-4 w-full bg-gray-100 rounded-lg" 
            placeholder="Change Topic Name?"
            ></Field>
          </div> -->
    <div>
    <p>This is SayText, {{ sayText }}</p>
    
  </div>
  </div>
</template>


<script>
import axios from 'axios'
import { Form, Field, ErrorMessage } from 'vee-validate';
import ChildGreeting from '../components/ChildGreeting.vue'




export default{
  name: 'showBlogView',
  components: {
    Form,
    Field,
    ErrorMessage,
    'child-greeting': ChildGreeting,
  
  },
  
  data() {
    return {
      itemId: '',
      item: null,
      sayText: '',
      fName: 'Jane',
      lName: 'Roe',
      

    }
  },

  mounted() {

    this.itemId = this.$route.params.id;
    // console.log('itemId: ', this.itemId)
    this.getFeed()
  },

  computed: {
    fullName() {
      return this.fName+' '+this.lName
    }
  },

  watch: {
  '$route.params.id'(newId, oldId) {
    // เรียกใช้งานฟังก์ชัน getFeed() เมื่อพารามิเตอร์ id เปลี่ยนค่า
    this.getFeed();
  }
},

  
  methods: {

    onSubmit() {
      console.log( 'Submitting :(', this.sayText );
    },

    getFeed() {
      axios
        .get(`/api/blog/topic/${this.$route.params.id}/`)
        .then(response => {
          console.log('getitem', response.data)
          this.item = response.data;
          

        })
        .catch(error => {
          console.log('error1',error)
        })
    },

    validateEmail(value) {
      // if the field is empty
      if (!value) {
        return 'This field is required';
      }

      // // if the field is not a valid email
      // const regex = /^[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,4}$/i;
      // if (!regex.test(value)) {
      //   return 'This field must be a valid email';
      // }

            // if the field contains only numbers
      if (/^\d+$/.test(value)) {
        return 'This field cannot be a number';
      }
      
      // All is good
      return true;
    },


  }
}
</script>
