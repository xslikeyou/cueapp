<template>
    <div>
      <h1>Ask a Question</h1>
      <input v-model="questionText" type="text" placeholder="Type your question...">
      <button @click="submitQuestion">Submit</button>
      <div v-if="answer">
        <h2>Answer:</h2>
        <p>{{ answer }}</p>
      </div>
    </div>
  </template>
  
  <script>
  import { ref } from 'vue';
  
  export default {
    name: 'QuestionView',
    setup() {
      const questionText = ref('');
      const answer = ref('');
  
      const submitQuestion = async () => {
        try {
          const response = await fetch('http://localhost:5000/answer', {
            method: 'POST',
            headers: {
              'Content-Type': 'application/json'
            },
            body: JSON.stringify({ question: questionText.value })
          });
  
          if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
          }
  
          const data = await response.json();
          answer.value = data.answer;
        } catch (error) {
          console.error('Error submitting question:', error);
        }
      };
  
      return {
        questionText,
        answer,
        submitQuestion
      };
    }
  }
  </script>