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
        <el-table-column align="center" label="名称">
          <template slot-scope="scope">
            <span>{{scope.row.name}}</span>
          </template>
        </el-table-column>
        <el-table-column align="center" label="任务">
          <template slot-scope="scope">
            <span>{{scope.row.task}}</span>
          </template>
        </el-table-column>
        <el-table-column align="center" label="调度类型">
          <template slot-scope="scope">
            <span v-if="scope.row.crontab">{{scope.row.crontab}}</span>
            <span v-else-if="scope.row.interval">{{scope.row.interval}}</span>
            <span v-else>-</span>
          </template>
        </el-table-column>
        <el-table-column align="center" label="入参">
          <template slot-scope="scope">
            <span>{{scope.row.args}}</span>
          </template>
        </el-table-column>
        <el-table-column align="center" label="参数">
          <template slot-scope="scope">
            <span>{{scope.row.kwargs}}</span>
          </template>
        </el-table-column>
        <el-table-column align="center" label="更改时间">
          <template slot-scope="scope">
            <span>{{scope.row.date_changed}}</span>
          </template>
        </el-table-column>
        <el-table-column align="center" label="运行次数">
          <template slot-scope="scope">
            <span>{{scope.row.total_run_count}}</span>
          </template>
        </el-table-column>
        <el-table-column align="center" label="过期时间">
          <template slot-scope="scope">
            <span>{{scope.row.expires}}</span>
          </template>
        </el-table-column>
        <el-table-column align="center" label="是否激活">
          <template slot-scope="scope">
            <span v-if="scope.row.enabled">激活</span>
            <span v-else>禁用</span>
          </template>
        </el-table-column>
        <el-table-column align="center" label="操作">
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
        <el-form-item :label="'序列'" prop="id">
          <el-input placeholder="不用填写" v-model="temp.id" readonly="true">
          </el-input>
        </el-form-item>
        <el-form-item :label="'名称'" prop="name">
          <el-input placeholder="Please input" v-model="temp.name">
          </el-input>
        </el-form-item>
        <el-form-item :label="'任务'" prop="task">
          <el-select v-model="temp.task" placeholder="请选择">
            <el-option v-for="item in regTask" :key="item.value"
            :label="item.label" :value="item.value">
            </el-option>
           </el-select>
        </el-form-item>
        <el-form-item :label="'调度类型'" prop="taskType">
          <el-select v-model="taskType" clearable placeholder="请选择">
            <el-option :key="'crontab'" :label="'Crontab'" :value="'crontab'">
            </el-option>
            <el-option :key="'interval'" :label="'Interval'" :value="'interval'">
            </el-option>
          </el-select>
        </el-form-item>
        <el-form-item v-if="taskType=='crontab'" :label="'Crontab'" prop="crontab">
          <el-select v-model="temp.crontab" clearable placeholder="请选择">
            <el-option :key="'crontab'" :label="'Crontab'" :value="'crontab'">
            </el-option>
            <el-option :key="'interval'" :label="'Interval'" :value="'interval'">
            </el-option>
          </el-select>
        </el-form-item>
        <el-form-item v-else-if="taskType=='interval'" :label="'Interval'" prop="interval">
          <el-select v-model="temp.crontab" clearable placeholder="请选择">
            <el-option :key="'crontab'" :label="'Crontab'" :value="'crontab'">
            </el-option>
            <el-option :key="'interval'" :label="'Interval'" :value="'interval'">
            </el-option>
          </el-select>
        </el-form-item>
        <el-form-item :label="'入参'" prop="args">
          <el-input placeholder="Please input" v-model="temp.args">
          </el-input>
        </el-form-item>
        <el-form-item :label="'参数'" prop="kwargs">
          <el-input placeholder="Please input" v-model="temp.kwargs">
          </el-input>
        </el-form-item>
        <el-form-item :label="'过期时间'" prop="expires">
          <el-date-picker v-model="temp.expires" type="datetime" placeholder="选择日期时间">
          </el-date-picker>
        </el-form-item>
        <el-form-item :label="'是否激活'" prop="enabled">
          <el-switch v-model="temp.enabled" active-text="激活" inactive-text="禁用">
          </el-switch>
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
import { fetchList, updateList, createList, deleteList, fetchRegTask } from '@/api/task'

export default {
  name: 'Task',
  data() {
    return {
      baseid: 'task', // 控制请求的url
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
        name: '',
        task: '',
        crontab: '',
        interval: '',
        args: '',
        kwargs: '',
        date_changed: '',
        total_run_count: '',
        expires: '',
        enabled: ''
      },
      taskType: '', // 模态框中的调度类型
      // 模态框
      dialogFormVisible: false,
      dialogStatus: '',
      textMap: {
        update: '编辑',
        create: '创建'
      },
      rules: {
      },
      regTask: []
    }
  },
  created() {
    this.getList()
    this.getRegTassk()
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
      this.$refs['dataForm'].validate(valid => {
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
        name: '',
        task: '',
        crontab: '',
        interval: '',
        args: '',
        kwargs: '',
        expires: '',
        enabled: ''
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
      this.$refs['dataForm'].validate(valid => {
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
      })
        .then(() => {
          deleteList(this.baseid, row.id).then(() => {
            this.$notify({
              title: '成功',
              message: '删除成功',
              type: 'success',
              duration: 2000
            })
            this.getList()
          })
        })
        .catch(() => {
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
    },
    getRegTassk() {
      fetchRegTask().then(response => {
        response.forEach(element => {
          this.regTask.push({ value: element, label: element })
        })
      })
    }
  }
}
</script>

<style scoped>
</style>
