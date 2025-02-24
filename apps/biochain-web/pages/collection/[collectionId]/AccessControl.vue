<script lang="ts" setup>

import UserCard from '~/components/Collection/UserCard.vue';

definePageMeta({
  auth: true,

  components: {
    UserCard
  },
})

const users = ref([
  { id: 1, name: 'Alice', role: "Admin" },
  { id: 2, name: 'Bob', role: "Manager" },
  { id: 3, name: 'Charlie', role: "Student" }
]);

</script>

<template>
  <h2 class="header">
    Access Control
    <UserCard v-for="user in users" :key="user.id" :user="user" />
  </h2>
</template>

<style scoped>
.header {
  font-weight: bold;
  padding-left: 16px;
  padding-top: 16px;
}
</style>
