<template>
  <div>
      <cron-task></cron-task>
      <interval-task></interval-task>
      <task></task>
  </div>
</template>

<script>
import { cronTask, intervalTask, Task } from './components'

export default {
  name: 'taskList',
  components: {
    cronTask,
    intervalTask,
    Task
  }
}
</script>

<style rel="stylesheet/scss" lang="scss" scoped>
</style>
