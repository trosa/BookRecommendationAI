<template>
  <div class="container-fluid">
    <h2 class="text-center mt-4 mb-4 text-white">GPT Book Recommendations</h2>
    <div class="">
      <form @submit.prevent="submitForm" class="bg-dark text-white p-4 rounded-lg">
        <label for="text-input" class="text-white">Name the last 5 books you've read:</label>
        <div class="form-group">
          <input type="text" id="text-input-1" v-model="inputText1" class="form-control mb-3 w-100">
          <input type="text" id="text-input-2" v-model="inputText2" class="form-control mb-3 w-100">
          <input type="text" id="text-input-3" v-model="inputText3" class="form-control mb-3 w-100">
          <input type="text" id="text-input-4" v-model="inputText4" class="form-control mb-3 w-100">
          <input type="text" id="text-input-5" v-model="inputText5" class="form-control mb-3 w-100">
        </div>
        <button type="submit" class="btn btn-primary btn-block">
          <span v-if="!isLoading">Get Recommendations</span>
          <span v-else class="spinner-border spinner-border-sm" role="status" aria-hidden="true"></span>
        </button>
      </form>
      <div v-if="apiResponse" class="api-response p-4 rounded-lg shadow-sm bg-dark">
        <h3 class="text-light">Our recommendation</h3>
        <p>{{ apiResponse }}</p>
      </div>
    </div>
  </div>
</template>

<style scoped>
/* Form styling */
form {
  background-color: #343a40; /* Darker background for contrast */
  color: #fff;
  border-radius: 10px; /* Increased border radius */
}

.form-group .form-control {
  width: 100%; /* Ensure full width for responsiveness */
}

label {
  color: #fff; /* Ensure label visibility */
}

.form-group {
  margin-bottom: 15px; /* Increased spacing between fields */
}

/* Button styling */
button {
  background-color: #007bff; /* Primary blue */
  border-color: #007bff;
  border-radius: 5px; /* Slightly rounded edges */
}

/* Response styling */
.api-response {
  background-color: #f8f9fa; /* Light gray background */
  border-color: #ddd;
  border-radius: 10px; /* Increased border radius */
  font-size: 16px; /* Slightly larger font for readability */
}

.container-fluid {
  width: 600px;
}
</style>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      inputText1: 'Outlive',
      inputText2: 'The Obesity Code',
      inputText3: 'Never Finished',
      inputText4: 'Cant Hurt Me',
      inputText5: 'Thinking, Fast and Slow',
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
          //this.inputText1 = '';
          //this.inputText2 = '';
          //this.inputText3 = '';
          //this.inputText4 = '';
          //this.inputText5 = '';
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

.api-response {
  border: 1px solid #ccc;
  padding: 15px;
  border-radius: 5px;
}
</style>