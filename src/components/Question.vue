<template>
    <!-- <div>
      <h1>Home Page</h1>
      <router-link to="/question">Ask a Question</router-link>
    </div> -->
    <div class="logo-container">
      <img src="../assets/vue.svg" alt="Logo">
    </div>
    <div id="qanda">
      <h1>Ask a Question</h1>
      <input v-model="questionText" type="text" placeholder="Type your question...">
      <button @click="submitQuestion">Submit</button>
      <div v-if="answer">
        <h2>Answer:</h2>
        <p class="answer">{{ answer }}</p>
      </div>
    </div>
  </template>
  
  <script setup>
  import axios from 'axios';
  import { ref } from 'vue';
  const questionText = ref('');
  const answer = ref('');

  const submitQuestion = async () => {
    try {
      // 使用 Axios 发送 POST 请求
      const response = await axios.post('http://localhost:8899/answer', {
        question: questionText.value
      });

      // 从响应中获取数据
      answer.value = response.data.answer;
    } catch (error) {
      // 错误处理
      console.error('Error submitting question:', error);
    }
  };

  </script>

<style scoped>
.answer{
  background-color: #0000ff; /* 蓝色背景 */
}
.logo-container img {
  position: fixed;
  top: 0;
  left: 0;
  z-index: 1000; /* 确保 logo 在其他内容的上方 */
  width: 50px; /* 或者任何你希望的尺寸 */
  height: auto;
}
#qanda{  
    position: absolute; /* 或 relative、fixed */
    top: 50px;
    left: 30px;
    border: 2px solid #000; /* 黑色实线边框 */
    padding: 20px; /* 内边距 */
    margin: 10px; /* 外边距 */
    width: 200px;
    height: 400px;
    background-color: antiquewhite;
  /* 其他样式 */
}
</style>