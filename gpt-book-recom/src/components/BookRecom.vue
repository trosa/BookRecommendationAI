<template>
  <div class="container">
    <h2 class="text-center mt-4 mb-4">GPT Book Recommendations</h2>
    <form @submit.prevent="submitForm" class="col-md-6 offset-md-3">
      <label for="text-input">Name the last 5 books you've read:</label>
      <div class="form-group">
        <input type="text" id="text-input-1" v-model="inputText1" class="form-control mb-3">
        <input type="text" id="text-input-2" v-model="inputText2" class="form-control mb-3">
        <input type="text" id="text-input-3" v-model="inputText3" class="form-control mb-3">
        <input type="text" id="text-input-4" v-model="inputText4" class="form-control mb-3">
        <input type="text" id="text-input-5" v-model="inputText5" class="form-control mb-3">
      </div>
      <button type="submit" class="btn btn-primary" :disabled="isLoading">
        <span v-if="!isLoading">Get Recommendations</span>
        <span v-else class="spinner-border spinner-border-sm" role="status" aria-hidden="true"></span>
      </button>
    </form>
    <div v-if="apiResponse" class="api-response mt-4">
      <h3>Recommended Books:</h3>
      <ul>
        <li v-for="book in apiResponse" :key="book.id">
          {{ book }}
        </li>
      </ul>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      inputText1: '',
      inputText2: '',
      inputText3: '',
      inputText4: '',
      inputText5: '',
      apiResponse: null,
      isLoading: false
    };
  },
  methods: {
    submitForm() {
      this.isLoading = true;
      axios.post('http://localhost:5000/books', {
        books: [
          this.inputText1,
          this.inputText2,
          this.inputText3,
          this.inputText4,
          this.inputText5
        ]
      })
        .then(response => {
          this.apiResponse = response.data;
          // Clear input fields after submission
          this.inputText1 = '';
          this.inputText2 = '';
          this.inputText3 = '';
          this.inputText4 = '';
          this.inputText5 = '';
          this.isLoading = false;
        })
        .catch(error => {
          console.error('API error:', error);
          this.isLoading = false; // Reset loading state on error too
          // Handle API errors gracefully, e.g., display an error message to the user
        });
    }
  }
};
</script>

<style scoped>
.illustration-container {
  text-align: center;
  margin-bottom: 20px;
}

.books-illustration {
  width: 300px;
  height: 200px;
}

.api-response {
  border: 1px solid #ccc;
  padding: 15px;
  border-radius: 5px;
}
</style>