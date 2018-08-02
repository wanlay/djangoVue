<template>

  <div class="app-container calendar-list-container">
    <el-card shadow="hover">
      <div slot="header" class="clearfix">
        <strong>任务详情</strong>
      </div>
      <div class="filter-container">
        <el-input @keyup.enter.native="handleFilter" style="width: 200px;" class="filter-item" :placeholder="'输入关键词'"
                  v-model="listQuery.search">
        </el-input>
        <el-button class="filter-item" type="primary" icon="el-icon-search" @click="handleFilter">搜索</el-button>
        <el-button class="filter-item" style="margin-left: 10px;" @click="handleCreate" type="primary"
                   icon="el-icon-edit">创建
        </el-button>
      </div>
      <el-table :data="list" v-loading.body="listLoading" border highlight-current-row style="width: 100%">
        <el-table-column align="center" label="序列" width="100%">
          <template slot-scope="scope">
            <span>{{scope.row.id}}</span>
          </template>
        </el-table-column>
        <el-table-column align="center" label="分">
          <template slot-scope="scope">
            <span>{{scope.row.minute}}</span>
          </template>
        </el-table-column>
        <el-table-column align="center" label="时">
          <template slot-scope="scope">
            <span>{{scope.row.hour}}</span>
          </template>
        </el-table-column>
        <el-table-column align="center" label="周">
          <template slot-scope="scope">
            <span>{{scope.row.day_of_week}}</span>
          </template>
        </el-table-column>
        <el-table-column align="center" label="月">
          <template slot-scope="scope">
            <span>{{scope.row.day_of_month}}</span>
          </template>
        </el-table-column>
        <el-table-column align="center" label="年">
          <template slot-scope="scope">
            <span>{{scope.row.month_of_year}}</span>
          </template>
        </el-table-column>
        <el-table-column align="center" label="Actions" width="300%">
          <template slot-scope="scope">
            <el-button-group>
              <el-button @click="handleUpdate(scope.row)" type="primary" size="mini" icon="el-icon-edit">编辑</el-button>
              <el-button @click="handleDelete(scope.row)" type="danger" size="mini" icon="el-icon-delete">删除</el-button>
            </el-button-group>
          </template>
        </el-table-column>
      </el-table>

      <div class="pagination-container">
        <el-pagination background @size-change="handleSizeChange" @current-change="handleCurrentChange"
                       :current-page="listQuery.page" :page-sizes="[5,8,10]" :page-size="listQuery.page_size"
                       layout="total, sizes, prev, pager, next, jumper" :total="total">
        </el-pagination>
      </div>
    </el-card>


    <el-dialog :title="textMap[dialogStatus]" :visible.sync="dialogFormVisible">
      <el-form ref="dataForm" :model="temp" :rules="rules" label-position="left" label-width="90px"
               style='width: 400px; margin-left:50px;'>
        <el-form-item :label="序列" prop="id">
          <el-input placeholder="不用填写" v-model="temp.id" disabled="true">
          </el-input>
        </el-form-item>
        <el-form-item :label="分" prop="minute">
          <el-input placeholder="Please input" v-model="temp.minute">
          </el-input>
        </el-form-item>
        <el-form-item :label="时" prop="hour">
          <el-input placeholder="Please input" v-model="temp.hour">
          </el-input>
        </el-form-item>
        <el-form-item :label="周" prop="day_of_week">
          <el-input placeholder="Please input" v-model="temp.day_of_week">
          </el-input>
        </el-form-item>
        <el-form-item :label="月" prop="day_of_month">
          <el-input placeholder="Please input" v-model="temp.day_of_month">
          </el-input>
        </el-form-item>
        <el-form-item :label="年" prop="month_of_year">
          <el-input placeholder="Please input" v-model="temp.month_of_year">
          </el-input>
        </el-form-item>
      </el-form>
      <div slot="footer" class="dialog-footer">
        <el-button @click="dialogFormVisible = false">取消</el-button>
        <el-button v-if="dialogStatus=='create'" type="primary" @click="createData">创建</el-button>
        <el-button v-else type="primary" @click="updateData">确认</el-button>
      </div>
    </el-dialog>
  </div>
</template>

<script>
  import { fetchList, updateList, createList, deleteList } from '@/api/task'

  export default {
    name: 'cronTask',
    data() {
      return {
        baseid: 'crontab',
        list: null,
        listLoading: true,
        total: null,
        listQuery: {
          page: 1,
          page_size: 5,
          search: undefined
        },
        temp: {
          id: '',
          minute: '',
          hour: '',
          day_of_week: '',
          day_of_month: '',
          month_of_year: ''
        },
        // 模态框
        dialogFormVisible: false,
        dialogStatus: '',
        textMap: {
          update: 'Edit',
          create: 'Create'
        }
      }
    },
    created() {
      this.getList()
    },
    methods: {
      getList() {
        this.listLoading = true
        fetchList(this.listQuery, this.baseid).then(response => {
          this.list = response.results
          this.total = response.count
          this.listLoading = false
        })
      },
      handleFilter() {
        this.listQuery.offset = 0
        this.getList()
      },
      handleUpdate(row) {
        this.temp = Object.assign({}, row) // copy obj
        this.dialogFormVisible = true
        this.dialogStatus = 'update'
        this.$nextTick(() => {
          this.$refs['dataForm'].clearValidate()
        })
      },
      updateData() {
        this.$refs['dataForm'].validate((valid) => {
          if (valid) {
            const tempData = Object.assign({}, this.temp)
            console.log(tempData)
            updateList(tempData, this.baseid, this.temp.id).then(() => {
              for (const v of this.list) {
                if (v.id === this.temp.id) {
                  const index = this.list.indexOf(v)
                  this.list.splice(index, 1, this.temp)
                  break
                }
              }
              this.dialogFormVisible = false
              this.$notify({
                title: '成功',
                message: '更新成功',
                type: 'success',
                duration: 2000
              })
            })
          }
        })
      },
      resetTemp() {
        this.temp = {
          minute: '',
          hour: '',
          day_of_week: '',
          day_of_month: '',
          month_of_year: ''
        }
      },
      handleCreate() {
        this.resetTemp()
        this.dialogStatus = 'create'
        this.dialogFormVisible = true
        this.$nextTick(() => {
          this.$refs['dataForm'].clearValidate()
        })
      },
      createData() {
        this.$refs['dataForm'].validate((valid) => {
          if (valid) {
            createList(this.temp, this.baseid).then(() => {
              this.list.unshift(this.temp)
              this.dialogFormVisible = false
              this.$notify({
                title: '成功',
                message: '创建成功',
                type: 'success',
                duration: 2000
              })
              this.getList()
            })
          }
        })
      },
      handleDelete(row) {
        this.$confirm('此操作将永久删除, 是否继续?', '提示', {
          confirmButtonText: '确定',
          cancelButtonText: '取消',
          type: 'warning'
        }).then(() => {
          deleteList(this.baseid, row.id).then(() => {
            this.$notify({
              title: '成功',
              message: '删除成功',
              type: 'success',
              duration: 2000
            })
            this.getList()
          })
        }).catch(() => {
          this.$message({
            type: 'info',
            message: '已取消删除'
          })
        })
      },
      handleSizeChange(val) {
        this.listQuery.page_size = val
        this.getList()
      },
      handleCurrentChange(val) {
        this.listQuery.page = val
        this.getList()
      }
    }
  }
</script>

<style scoped>
</style>
