<template>
    <UCard>
        <Placeholder class="py-10">
            <div class="flex flex-row justify-between">
                <div>
                    <h3>{{ user.name }}</h3>
                    <p>Role: {{ user.role }}</p>
                </div>
                <div flex justify-center items-center>
                    <UDropdown :items="items" :popper="{ placement: 'bottom-start' }">
                        <UButton color="white" label="Options" trailing-icon="i-heroicons-chevron-down-20-solid" />
                    </UDropdown>
                </div>
            </div>
        </Placeholder>
    </UCard>
</template>

<!-- <script>
export default {
  props: {
    user: Object
  },
  data() {
    return {
      items: [
        [
          {
            label: 'Profile',
            avatar: {
              src: 'https://avatars.githubusercontent.com/u/739984?v=4'
            },
            disabled: true,
            class: "text-blue-500 opacity-100"
          },
          {
            label: 'Profile',
            avatar: {
              src: 'https://avatars.githubusercontent.com/u/739984?v=4'
            }
          }
        ],
        [
          {
            label: 'Edit',
            icon: 'i-heroicons-pencil-square-20-solid',
            shortcuts: ['E'],
            click: () => {
              console.log('Edit');
            }
          },
          {
            label: 'Duplicate',
            icon: 'i-heroicons-document-duplicate-20-solid',
            shortcuts: ['D'],
            disabled: true
          }
        ],
        [
          {
            label: 'Archive',
            icon: 'i-heroicons-archive-box-20-solid'
          },
          {
            label: 'Move',
            icon: 'i-heroicons-arrow-right-circle-20-solid'
          }
        ],
        [
          {
            label: 'Delete',
            icon: 'i-heroicons-trash-20-solid',
            shortcuts: ['⌘', 'D']
          }
        ]
      ]
    };
  }
};
</script> -->

<script>
export default {
    props: {
        user: Object
    },
    data() {
        return {
            items: [
                [
                    {
                        label: 'Edit',
                        icon: 'i-heroicons-pencil-square-20-solid',
                        click: () => {
                            console.log('Edit');
                        }
                    },

                ],
                [
                    {
                        label: 'Set role',
                        disabled: true,
                        class: "opacity-100",
                    },
                    {
                        label: 'Admin',
                        class: "font-normal",
                        click: () => {
                            console.log('Setting admin');
                        }
                    },
                    {
                        label: 'Manager',
                        class: "font-normal",
                        click: () => {
                            console.log('Setting role 1');
                        },
                    },
                    {
                        label: 'Student',
                        class: "font-normal",
                        click: () => {
                            console.log('Setting role 1');
                        },
                    },
                ],
                [
                    {
                        label: 'Delete the user',
                        icon: 'i-heroicons-trash-20-solid',
                        click: () => {
                            console.log('Deleting user');
                        }
                    }
                ]
            ]
        };
    }
};
</script>

<style scoped>
.card {
    padding: 10px;
}

.dropdowntext {
    color: blue;
}
</style>