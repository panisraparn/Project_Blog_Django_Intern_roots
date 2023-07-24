import './assets/main.css'

import { createApp } from 'vue'
import { createPinia } from 'pinia'

import App from './App.vue'
import router from './router'
import axios from 'axios'
import { defineRule, configure } from 'vee-validate';
import { required } from '@vee-validate/rules';

axios.defaults.baseURL = 'http://127.0.0.1:8001/'
const app = createApp(App)

// กำหนดกฎการตรวจสอบ
defineRule('required', required);

// กำหนดการกำหนดค่าเริ่มต้นของ VeeValidate
configure({
  validateOnInput: true, // ทำการตรวจสอบความถูกต้องขณะป้อนข้อมูล
  validateOnChange: true, // ทำการตรวจสอบความถูกต้องเมื่อมีการเปลี่ยนค่า
});

app.use(createPinia())
app.use(router, axios)

app.mount('#app')
