<template>
<div class="max-w-7xl max-auto grid grid-cols-4 gap-4">
  
  <div class="main-left col-span-2">
    <div class="p-4 bg-white border border-gray-200 text-center rounded-lg">
      <p><strong>{{ userStore.user.name }}</strong></p>
      <div class="p-4 bg-white border border-gray-200 text-center rounded-lg">
        
        
        <!-- component event -enits -->
        <button @click="isMenuOpen = true" class="inline-block py-4 px-6 bg-yellow-800 text-white rounded-lg" >Open Menu</button>
        <!-- <main-menu v-if="isMenuOpen" @closeMenu="isMenuOpen = false" /> -->
        <main-menu v-if="isMenuOpen" @closeMenu="closeMenu" />
        <p><strong>{{ nameMenu }}</strong></p>
      </div>

     
      <!-- <form v-on:submit.prevent="submitForm" method="post">
          <div class="p-4">
            <textarea v-model="name" class="p-4 w-full bg-gray-100 rounded-lg" placeholder="add topic name?"></textarea>
          </div>
          
          <div class="p-4 border-t border-yellow-100 flex justify-center">
            <button href="#" class="inline-block py-4 px-6 bg-yellow-800 text-white rounded-lg">Post</button>
          </div>
      </form> -->
      <p><strong> ---Topic--- </strong></p>
      <Form @submit="submitForm" method="post">
        
        <div class="p-4">
          <Field 
            type="textarea"
            name="nameTopic"
            v-model="name" 
            class="p-4 w-full bg-gray-100 rounded-lg" 
            placeholder="add topic name?" 
            :rules="validateTopicName"
          />
          <ErrorMessage name="nameTopic" />
        </div>
          
        <div class="p-4 border-t border-yellow-100 flex justify-center">
          <button href="#" class="inline-block py-4 px-6 bg-yellow-800 text-white rounded-lg">Post</button>
        </div>
      </Form>
  </div>
  
    <div class="p-4 bg-white border border-gray-200 text-center rounded-lg">
      <div  v-for="topic in topics" >
      
          <p><strong> {{topic.id}}-{{ topic.name }}  </strong></p>
        <div class="p-4  flex justify-center">
          <button @click="deleteTopic(topic.id)" class="inline-block py-4 px-6 bg-gray-600 text-white rounded-lg">Delete</button>
          <!-- <button @click="selectTopic(topic)" class="inline-block py-4 px-6 bg-purple-600 text-white rounded-lg">View</button> -->
        </div>

      </div>
    </div>

         <div class="p-4 bg-white border border-gray-200 rounded-lg"   
      v-for="(topic, index) in topics" :key="index"

      >
        <div class="mb-6 flex items-center justify-between">


          <!-- header ของ Post -->
          <div class="flex items-center space-x-6">
            
      
              <!-- ../profile/id -->
              <RouterLink :to="{'name': 'show', params:{'id': topic.id} }">
                <p><strong> {{topic.name}} </strong></p>
              </RouterLink>
              <!-- <RouterLink :to="`/show/${topic.object.id}`">
                <p><strong>{{topic.name}}</strong></p>
              </RouterLink>
        -->
  
          </div>
          
        </div>

        <!-- center ของ post -->
        <div class="bg-white border border-gray-200  rounded-lg">
          <form v-on:submit.prevent="updateTopicForm" method="put">
          <div class="p-4">
            <textarea v-model="updatedName" class="p-4 w-full bg-gray-100 rounded-lg" placeholder="Change Topic Name?"></textarea>
          </div>
          
        
          <div class="p-4  flex justify-end">
            <button @click="update(index)" class="inline-block py-4 px-6 bg-purple-600 text-white rounded-lg">Update</button>
          </div>
        </form>
      </div>

        <!-- bottom ของ post -->
        <div class="my-6 flex justify-between">
          
          <div class="flex space-x-6">
            
   
          
          </div>
          
   
        
        </div>
      
      </div>


    
  </div>




  <div class="main-center col-span-2 space-y-4">
    
    <div class="p-4 bg-white border border-gray-200 text-center rounded-lg">
      <RouterView/>
      
    </div>
    

  </div>
    
    
</div>


    

</template>

<script>
import axios from 'axios'
import { useUserStore } from '@/stores/user'
import { Form, Field, ErrorMessage } from 'vee-validate';
import MainMenu from '../components/MainMenu.vue'

export default{
  name: 'BlogView',
  components: {
    Form,
    Field,
    ErrorMessage,
    'main-menu': MainMenu,
  },


 
    
  setup() {
    const userStore = useUserStore()
    
    return {
      userStore
      }
  },

  data() {
    return {
      topics: [],
      name: '', // ตัวแปรที่ผูกกับ v-model
      updatename: [],
      isMenuOpen: false,
      nameMenu: '',

    }
  },

  mounted() {
    this.getTopics()
  },
  
  methods: {
    getTopics(){
      axios
        .get('/api/blog/topic/')
        .then(response =>{
          this.topics = response.data
          console.log('Topics:', response.data)
        })
        .catch(error =>{
          console.error('errorGetTopics', error)
        })
    },

    
    
    submitForm() {
      console.log('submitForm', this.name)

      axios
        .post('/api/blog/topic/',{
          'name': this.name

        })
        .then(response => {
          console.log('data', response.data)

          // add เข้า array เพื่อไปแสดงผล
          this.topics.unshift(response.data) //add เข้า array แล้วเเสดงผลทันที
          this.name = '' //reset body

        })
        .catch(error => {
          console.log('error',error)
        })
    },

    deleteTopic(pk){
      // console.log(topic.id)
    
      axios
      .delete(`/api/blog/topic/delete/${pk}/`)
      .then(response => {
        console.log(response.data);
        this.getTopics()
        
        })
        .catch(error => {
          console.error(error); 
          });
    },
    
      update(index) {
        // console.log(this.updatename);
        console.log(this.topics[index].id);
        const topicId = this.topics[index].id;
        const updatedName = this.topics[index].name;
        
        axios.put(`/api/blog/topic/update/${topicId}/`, { name: this.updatedName })
        .then(response => {
          console.log('suceesupdate2:',response.data);
          this.updatedName = '' //reset body
          this.getTopics() 
        })
        .catch(error => {
          console.error(error); 
        });
    },

      validateTopicName(value) {
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
    closeMenu(data) {
      this.isMenuOpen = false;
      this.nameMenu = data;

    },
  
}


  }

</script>
