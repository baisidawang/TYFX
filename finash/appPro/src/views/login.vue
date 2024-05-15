<template>
    <div class="login-container">
      <el-card class="login-card">
        <h2 class="login-title">Welcome</h2>
        <el-form :model="loginForm" label-width="80px">
          <el-form-item label="Username" prop="username">
            <el-input v-model="loginForm.username" placeholder="Enter your username"></el-input>
          </el-form-item>
          <el-form-item label="Password" prop="password">
            <el-input v-model="loginForm.password" type="password" placeholder="Enter your password"></el-input>
          </el-form-item>
          <el-form-item>
            <el-button type="primary" @click="login">Login</el-button>
          </el-form-item>
        </el-form>
      </el-card>
    </div>
  </template>
  
  <script setup>
  import { ref } from 'vue';
  import { defineComponent } from 'vue';
  import { useRouter } from 'vue-router';

  const router = useRouter();
  
  const loginForm = ref({
    username: '',
    password: ''
  });
  
  const login = () => {

    router.push('/index')
    
  };
  </script>
  
  <style scoped>
  .login-container {
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100vh;
  }
  
  .login-card {
    width: 400px;
  }
  
  .login-title {
    text-align: center;
    margin-bottom: 20px;
  }
  </style>
  