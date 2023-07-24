import { defineStore } from 'pinia'

export const useToastStore = defineStore({
  id: 'toast',

  //defaulstate
  state: () => ({
    ms: 0, //เวลาที่แสดงข้อความ
    message: '',
    classes: '',// คลาส CSS ที่ใช้กับ Toast
    isVisible: false
  }),

  actions: {
    showToast(ms, message, classes){
      this.ms = parseInt(ms)
      this.message = message
      this.classes = classes
      this.visible = true

      setTimeout(() => {
        this.classes += 'translate-y-28' // เพิ่มคลาส CSS 'translate-y-28' เข้าไปใน this.classes หลังจากผ่านไป 10 มิลลิวินาที
      },10)

      setTimeout(() => {
        this.classes = this.classes.replace('translate-y-28','') // ลบคลาส CSS 'translate-y-28' ออกจาก this.classes หลังจากผ่านไประยะเวลาที่กำหนด (ms - 500) มิลลิวินาที
      }, this.ms - 500)

      setTimeout(() => {
        this.isVisible = false
      }, this.ms)
      
      // การใช้ (this.ms - 500) ในโค้ดนั้นหมายความว่าจะนำค่าของ this.ms ที่เก็บระยะเวลาของ Toast ที่กำหนดไว้ในสถานะของสโตร์ ลบด้วยจำนวน 500 มิลลิวินาที เพื่อให้ได้ระยะเวลาที่ Toast จะควรแสดง (แสดงเป็นมิลลิวินาที)
      // เมื่อถึงเวลาที่กำหนด (this.ms - 500) ใน setTimeout คลาส CSS 'translate-y-28' จะถูกเพิ่มใน this.classes เพื่อให้ Toast เคลื่อนย้ายลงมาแสดงให้ผู้ใช้เห็น ซึ่งเป็นการใช้คลาส CSS ในการสร้างเอฟเฟกต์แบบต่าง ๆ
      // หลังจากผ่านไปเวลาที่กำหนด (this.ms - 500) อีกครั้ง คลาส CSS 'translate-y-28' จะถูกลบออกจาก this.classes เพื่อทำให้ Toast เคลื่อนย้ายขึ้นเพื่อซ่อนตัวอย่างละเอียด

    }
  }

})
