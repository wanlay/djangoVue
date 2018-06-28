<template>
  <el-dialog
    title="提示"
    :visible.sync="dialogVisible"
    width="30%"
    center>
    <img class="image" :src="avatar+'?imageView2/1/w/80/h/80'">
    <span>name:{{name}}</span>
    roles:<span v-for='role in roles' :key='role'>{{role}}</span>
    <span slot="footer" class="dialog-footer">
    <el-button type="primary" @click="dialogVisible = false">确 定</el-button>
  </span>
  </el-dialog>
</template>

<script>
  import { mapGetters } from 'vuex'

  export default {
    data() {
      return {
        dialogVisible: true
      }
    },
    computed: {
      ...mapGetters([
        'avatar',
        'name',
        'roles'
      ])
    }
  }
</script>

<style rel="stylesheet/scss" lang="scss" scoped>
    .image {
    width: 10%;
    display: block;
  }
</style>
