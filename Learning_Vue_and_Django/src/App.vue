<script setup>
import { ref, reactive, computed }  from 'vue';

// ref is good for single values or primitive data types
// reactive is good for objects or arrays
// computed means that it is a function that returns a value that is derived from other reactive values
// example of computed is .filter(), .map(), .reduce(), .sort(), etc.
const name = ref("Eisblume")
const tasks = 
  reactive([
    { id: 1, title: "Learn Vue.js", completed: false },
    { id: 2, title: "Learn Django Rest Framework", completed: false },
    { id: 3, title: "Learn Axios", completed: false },
    { id: 4, title: "Learn Vue Routers", completed: false },
  ])

  const hide = ref(true)
  const hiddenTasks = computed(() => {
  return hide.value ? tasks.filter(task => task.completed) : tasks; // if hide is true, then show only the completed tasks
});

</script>

<template>
  <header>

   
  </header>

  <main>
    <div id="todo">
      <div class="container mt-5">
        <div class="row justify-content-md-center">
          <div class="col-md-8 bg-white p-3 rounded">
            {{ name }} To-do List

            <hr>

            <div class="row d-flex justify-content-between px-3 py-2" v-for="t in hiddenTasks" v-bind:key="t.task"> 
              <!-- v-for is for looping through an array and v-bind is for binding an attribute to a value -->
              <div>{{ t.title }}</div>
              <div>
                <input type="checkbox" v-model="t.completed" class="form-check-input" />
              </div>

              
            </div>

            <input type="checkbox" v-model="hide" class="form-check-input" />
            <label for="">Hide/Show</label>

          </div>
        </div>
      </div>
    </div>
  </main>
</template>


<style>

  body {
    background-color: darkcyan!important;
  }
</style>
