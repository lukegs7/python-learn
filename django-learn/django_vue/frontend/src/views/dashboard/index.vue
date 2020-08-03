<template>
  <div class="dashboard-container">
    <el-card class="box-card">
      <h3>环境列表</h3>
      <el-row style="margin-bottom:20px">
        <el-button style="float:right; width:10%" type="primary" @click="handleNew">新增环境</el-button>
        <el-input v-model="search" style="float:left; width:20%" placeholder="Type to search" @change="searchEnv" />
        <el-button style="float:left" icon="el-icon-search" @click="searchEnv" />
      </el-row>
      <el-row>
        <el-table
          :data="tableData"
          :header-cell-style="{'text-align':'center'}"
          :cell-style="{'text-align':'center'}"
          border
        >
          <el-table-column label="环境名称" prop="name" min-width="30" />
          <el-table-column label="url" prop="url" min-width="30">
            <template slot-scope="scope">
              <el-button type="text" @click="jump(scope.row.url)">{{ scope.row.url }}</el-button>
            </template>
          </el-table-column>
          <el-table-column label="状态" prop="status" min-width="10">
            <template slot-scope="scope">
              <i v-if="scope.row.status" class="el-icon-check" style="color:green;font-size:20px" />
              <i v-else class="el-icon-close" style="color:red;font-size:20px" />
            </template>
          </el-table-column>
          <el-table-column label="更新时间" prop="update_time" min-width="30" />
          <el-table-column label="备注" prop="remark" min-width="20" />
          <el-table-column label="操作" min-width="30">
            <template slot-scope="scope">
              <el-button type="primary" @click="handleEdit(scope.$index,scope.row)">编辑</el-button>
              <el-popover v-model="deleteVisible[scope.$index]" placement="top" width="160" trigger="click">
                <p><i class="el-icon-warning" />确定删除</p>
                <div style="text-align:right;margin:0">
                  <el-button size="mini" type="text" @click="closePopover(scope.$index)">取消</el-button>
                  <el-button size="mini" type="primary" @click="handleDelete(scope.$index,scope.row)">确定</el-button>
                </div>
                <el-button slot="reference" type="danger" style="margin-left:20px">删除</el-button>
              </el-popover>
            </template>
          </el-table-column>
        </el-table>
      </el-row>
    </el-card>
    <el-dialog
      :close-on-click-modal="false"
      :title="dialogType==='new'?'新建环境':'编辑环境'"
      :visible.sync="dialogShow"
      width="20%"
      center
    >
      <el-form ref="envForm" :model="form" label-width="80px">
        <el-form-item label="环境名称" prop="name">
          <el-input v-model="form.name" />
        </el-form-item>
        <el-form-item label="url" prop="url">
          <el-input v-model="form.url" />
        </el-form-item>
        <el-form-item label="在线状态" prop="status">
          <el-radio-group v-model="form.status">
            <el-radio :label="0">离线</el-radio>
            <el-radio :label="1">在线</el-radio>
          </el-radio-group>
        </el-form-item>
        <el-form-item label="备注" prop="remark">
          <el-input v-model="form.remark" />
        </el-form-item>
        <el-form-item>
          <el-button type="warn" @click="dialogShow=false">取消</el-button>
          <el-button @click="resetForm('envForm')">重置</el-button>
          <el-button type="primary" @click="submitForm">提交</el-button>
        </el-form-item>
      </el-form>
    </el-dialog>
  </div>
</template>

<script>
import { mapGetters } from 'vuex'

export default {
  name: 'Dashboard',
  data() {
    return {
      search: '',
      deleteVisible: [],
      tableDataRaw: [],
      tableData: [],
      dialogType: 'new',
      dialogShow: false,
      form: {
        name: '',
        url: '',
        status: 1,
        remark: ''
      }
    }
  },
  computed: {
    ...mapGetters([
      'name'
    ])
  },
  created() {
    this.defaultForm = JSON.parse(JSON.stringify(this.form))
  },
  mounted() {
    this.loadTable()
    this.tableData.forEach(el => {
      this.deleteVisible.push(false)
    })
  },
  methods: {
    loadTable() {
      this.getHttpData('environment/', '', data => {
        console.log(data.data.data)
        this.tableDataRaw = JSON.parse(JSON.stringify(data.data.data))
        this.tableData = data.data.data
      })
    },
    closePopover(index, row) {
      this.deleteVisible.splice(index, 1, false)
    },
    handleEdit(index, row) {
      this.dialogType = 'edit'
      this.dialogShow = true
      this.form = JSON.parse(JSON.stringify(row))
      this.form.id = row.id
    },
    handleNew() {
      this.form = Object.assign({}, this.defaultForm)
      this.dialogType = 'new'
      this.dialogShow = true
    },
    handleDelete(inde, row) {
      this.deleteHttpData('environment/' + row.id + '/', '', data => {
        this.$message({
          type: 'success',
          message: '删除成功'
        })
        this.loadTable()
      })
    },
    searchEnv() {
      this.tableData = this.tableDataRaw.filter(data => !this.search || data.name.toLowerCase().includes(this.search.toLowerCase()))
    },
    jump(new_url) {
      // 打开新的标签跳转
      var ref_url = new_url.replace(/(^\s*)|(\s*$)/g, '')
      if (ref_url.substr(0, 7) !== 'http://') {
        ref_url = 'http://' + ref_url
      }
      window.open(ref_url)
    },
    resetForm(formName) {
      if (this.$refs[formName]) {
        this.$refs[formName].resetFields()
      }
    },
    submitForm() {
      console.log(this.dialogType)
      if (this.dialogType === 'new') {
        this.postHttpData('environment/', this.form, data => {
          if (data.data.code === 0) {
            this.$message({
              type: 'success',
              message: data.data.msg
            })
            this.dialogShow = false
            this.loadTable()
          } else {
            this.$message({
              type: 'error',
              message: data.data.msg
            })
          }
        })
      } else {
        this.putHttpData('environment/' + this.form.id + '/', this.form, data => {
          if (data.data.code === 0) {
            console.log('return message', data.data.msg)
            this.dialogShow = false
            this.$message({
              type: 'success',
              message: data.data.msg
            })
            this.dialogShow = false
            this.loadTable()
          } else {
            this.$message({
              type: 'error',
              message: data.data.msg
            })
          }
        })
      }
    }
  }
}
</script>

<style lang="scss" scoped>
.dashboard {
  &-container {
    margin: 30px;
  }
  &-text {
    font-size: 30px;
    line-height: 46px;
  }
}
</style>
