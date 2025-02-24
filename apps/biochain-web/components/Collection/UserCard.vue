<template>
  <div class="card">
    <h3>{{ user.name }}</h3>
    <p>Role: {{ user.role }}</p>
  </div>
</template>

<script>
export default {
  props: {
    user: Object
  }
};
</script>

<style scoped>
.card {
  border: 1px solid #ddd;
  padding: 10px;
  margin-top: 10px;
  margin-bottom: 10px;
  border-radius: 5px;
}
</style>