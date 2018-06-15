<template>
  <div class="app-container calendar-list-container">
    <div class="filter-container">
      <el-input @keyup.enter.native="handleFilter" style="width: 200px;" class="filter-item" :placeholder="'输入关键词'"
                v-model="listQuery.search">
      </el-input>
      <el-button class="filter-item" type="primary" icon="el-icon-search" @click="handleFilter">搜索</el-button>
      <el-button class="filter-item" style="margin-left: 10px;" @click="handleCreate" type="primary"
                 icon="el-icon-edit">创建
      </el-button>
    </div>
    <el-table :data="list" v-loading.body="listLoading" border fit highlight-current-row style="width: 100%">
      <el-table-column align="center" label="ID" width="80">
        <template slot-scope="scope">
          <span>{{scope.row.id}}</span>
        </template>
      </el-table-column>
      <el-table-column align="center" label="版本名称" width="90">
        <template slot-scope="scope">
          <span>{{scope.row.service_name}}</span>
        </template>
      </el-table-column>
      <el-table-column align="center" label="版本路径" width="200">
        <template slot-scope="scope">
          <span>{{scope.row.path}}</span>
        </template>
      </el-table-column>
      <el-table-column align="center" label="涉及war包名" width="150">
        <template slot-scope="scope">
          <span>{{scope.row.package}}</span>
        </template>
      </el-table-column>
      <el-table-column align="center" label="发布机器IP" width="120">
        <template slot-scope="scope">
          <span>{{scope.row.location}}</span>
        </template>
      </el-table-column>
      <el-table-column align="center" label="版本" width="80">
        <template slot-scope="scope">
          <span>{{scope.row.version}}</span>
        </template>
      </el-table-column>
      <el-table-column align="center" label="发布日期" width="120">
        <template slot-scope="scope">
          <span>{{scope.row.date}}</span>
        </template>
      </el-table-column>
      <el-table-column align="center" label="发布人" width="100">
        <template slot-scope="scope">
          <span>{{scope.row.person}}</span>
        </template>
      </el-table-column>
      <el-table-column align="center" label="Actions" width="100">
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
                     :current-page="listQuery.offset/listQuery.limit+1" :page-sizes="[5,10,20,2,]" :page-size="listQuery.limit"
                     layout="total, sizes, prev, pager, next, jumper" :total="total">
      </el-pagination>
    </div>

    <el-dialog :title="textMap[dialogStatus]" :visible.sync="dialogFormVisible">
      <el-form ref="dataForm" :model="temp" label-position="left" label-width="70px"
               style='width: 400px; margin-left:50px;'>
        <el-form-item :label="'ID'" prop="id">
          <el-input placeholder="不用填写" v-model="temp.id" :disabled="true">
          </el-input>
        </el-form-item>
        <el-form-item :label="'版本名称'" prop="service_name">
          <el-input placeholder="Please input" v-model="temp.service_name">
          </el-input>
        </el-form-item>
        <el-form-item :label="'版本路径'" prop="path">
          <el-input type="textarea" autosize placeholder="Please input" v-model="temp.path">
          </el-input>
        </el-form-item>
        <el-form-item :label="'涉及war包名'" prop="package">
          <el-input type="textarea" autosize placeholder="Please input" v-model="temp.package">
          </el-input>
        </el-form-item>
        <el-form-item :label="'发布机器IP'" prop="location">
          <el-input placeholder="Please input" v-model="temp.location">
          </el-input>
        </el-form-item>
        <el-form-item :label="'版本'" prop="version">
          <el-select v-model="temp.version" placeholder="请选择">
            <el-option
              v-for="item in options"
              :key="item.value"
              :label="item.label"
              :value="item.value">
            </el-option>
          </el-select>
        </el-form-item>
        <el-form-item :label="'发布日期'" prop="date">
          <el-date-picker
            v-model="temp.date"
            type="date"
            placeholder="选择时间"
            value-format="yyyy-MM-dd" >
          </el-date-picker>
        </el-form-item>
        <el-form-item :label="'发布人'" prop="person">
          <el-input placeholder="Please input" v-model="temp.person">
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
  import { fetchList, updateList, createList, deleteList } from '@/api/table'

  export default {
    name: 'yiguandian',
    data() {
      return {
        list: null,
        listLoading: true,
        total: null,
        listQuery: {
          offset: 0,
          limit: 10,
          search: undefined
        },
        temp: {
          id: '',
          service_name: '',
          path: '',
          package: '',
          location: '',
          version: '',
          date: '',
          person: ''
        },
        // 模态框
        dialogFormVisible: false,
        dialogStatus: '',
        textMap: {
          update: 'Edit',
          create: 'Create'
        },
        // 选择器
        options: [{
          value: 'A',
          label: 'A'
        }, {
          value: 'B',
          label: 'B'
        }]
      }
    },
    created() {
      this.getList()
    },
    methods: {
      getList() {
        this.listLoading = true
        fetchList(this.listQuery).then(response => {
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
            updateList(tempData, this.temp.id).then(() => {
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
          service_name: '',
          path: '',
          package: '',
          location: '',
          version: '',
          date: '',
          person: ''
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
            createList(this.temp).then(() => {
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
          deleteList(row.id).then(() => {
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
        this.listQuery.limit = val
        this.getList()
      },
      handleCurrentChange(val) {
        this.listQuery.offset = this.listQuery.limit * (val - 1)
        this.getList()
      }
    }
  }
</script>

<style scoped>
</style>
