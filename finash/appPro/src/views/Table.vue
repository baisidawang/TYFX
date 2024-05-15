<template>
    <a-table :columns="columns" :data-source="date" :scroll="{ x: 3500, y: 900 }">
      <template #bodyCell="{ column, record }">
        <template v-if="column.key === 'operation'">
            <div>
                <a-button type="primary" @click="showDrawer(record)">
                    <template #icon><PlusOutlined /></template>
                    查看
                </a-button>
            </div>
            <br>
            
            <a-button type="primary" danger @click="dele(record)">
                <template #icon><PlusOutlined /></template>
                删除
            </a-button>
            <a-drawer
                title="信息表"
                :width="1000"
                :open="open"
                :body-style="{ paddingBottom: '80px' }"
                :footer-style="{ textAlign: 'right' }"
                @close="onClose"
                ref="pdfContent">
<div ref="tyfx">
  <el-descriptions title="退役复学信息表" :column="3" border >
    <el-descriptions-item label="id"     label-align="right" align="center" label-class-name="my-label" class-name="my-content" width="150px" >{{shuju.id}}</el-descriptions-item>
    <el-descriptions-item label="姓名" label-align="right" align="center" >{{shuju.name}}</el-descriptions-item>
    <el-descriptions-item label="性别" label-align="right" align="center" >{{shuju.gender}}</el-descriptions-item>
    <el-descriptions-item label="民族" label-align="right" align="center" >{{shuju.nation}}</el-descriptions-item>
    <el-descriptions-item label="出生日期" label-align="right" align="center" >{{shuju.birthday}}</el-descriptions-item>
    <el-descriptions-item label="政治面貌" label-align="right" align="center" >{{shuju.politic}}</el-descriptions-item>
    <el-descriptions-item label="学号" label-align="right" align="center" >{{shuju.Sno}}</el-descriptions-item>
    <el-descriptions-item label="户籍地" label-align="right" align="center" >{{shuju.domicile}}</el-descriptions-item>
    <el-descriptions-item label="身份证号" label-align="right" align="center" >{{shuju.ID_card}}</el-descriptions-item>
    <el-descriptions-item label="入伍时间" label-align="right" align="center" >{{shuju.enlist_time}}</el-descriptions-item>
    <el-descriptions-item label="退伍时间" label-align="right" align="center" >{{shuju.retire_time}}</el-descriptions-item>
    <el-descriptions-item label="入伍前班导师" label-align="right" align="center" >{{shuju.before_teacher}}</el-descriptions-item>
    <el-descriptions-item label="退伍后班导师" label-align="right" align="center" >{{shuju.retire_teacher}}</el-descriptions-item>
    <el-descriptions-item label="入伍前学院班级" label-align="right" align="center" >{{shuju.before_class}}</el-descriptions-item>
    <el-descriptions-item label="退伍后学院班级" label-align="right" align="center" >{{shuju.retire_class}}</el-descriptions-item>
    <el-descriptions-item label="服役部队" label-align="right" align="center" >{{shuju.searvice_troops}}</el-descriptions-item>
    <el-descriptions-item label="职务" label-align="right" align="center" >{{shuju.duties}}</el-descriptions-item>
    <el-descriptions-item label="本人电话" label-align="right" align="center" >{{shuju.number}}</el-descriptions-item>
    <el-descriptions-item label="家庭电话" label-align="right" align="center" >{{shuju.family_number}}</el-descriptions-item>
    <el-descriptions-item label="入伍地" label-align="right" align="center" >{{shuju.enlist_place}}</el-descriptions-item>
    <el-descriptions-item label="挂科科目" label-align="right" align="center" >{{shuju.pend}}</el-descriptions-item>
    <el-descriptions-item label="奖惩情况" label-align="right" align="center" >{{shuju.rewards}}</el-descriptions-item>  
    <el-descriptions-item label="个人照" label-align="right" align="center" >  <img :src="'data:image/png;base64,' + [ shuju.personal_photo ]" style="max-width: 100px; max-height: 100px;" /></el-descriptions-item>
    <el-descriptions-item label="本人签字" label-align="right" align="center" >  <img :src="'data:image/png;base64,' + [ shuju.sign_photo ]" style="max-width: 100px; max-height: 100px;" /></el-descriptions-item>
    
    <el-descriptions-item label="退役证" label-align="right" align="center" >  <img :src="'data:image/png;base64,' + [ shuju.retire_photo ]" style="max-width: 100px; max-height: 100px;" /></el-descriptions-item>  
    
    <el-descriptions-item label="专业培训及证书" label-align="right" align="center" >  <img :src="'data:image/png;base64,' + [ shuju.certifiate ]" style="max-width: 100px; max-height: 100px;" /></el-descriptions-item>
    <el-descriptions-item label="入伍通知书" label-align="right" align="center" >  <img :src="'data:image/png;base64,' + [ shuju.enlist_photo ]" style="max-width: 100px; max-height: 100px;" /></el-descriptions-item>

  </el-descriptions>
</div>


    <template #extra>
      <a-space>
        <a-button @click="onClose">退出</a-button>
        <a-button type="primary" @click="exportToPDF">导出PDF</a-button>
      </a-space>
    </template>
  </a-drawer>

        </template>
        <div v-else-if="column.key === 'base64'">
        <img v-if="record[column.dataIndex]" :src="'data:image/png;base64,' + record[column.dataIndex]" style="max-width: 100px; max-height: 100px;" /> 
       </div> 
       <div v-else-if="column.key === 'lm'">
          <div></div>
       </div>
      </template>  
      </a-table>
      <button @click="oo()">dianjiwo </button>
      <div>我是数据==={{shuju.id}}</div>
  </template>



  <script lang="ts" setup>
  import { reactive } from 'vue';
  import { ref } from 'vue';
  import axios from 'axios';
  import type { TableColumnsType } from 'ant-design-vue';
  import { onMounted } from 'vue';
  import jsPDF from 'jspdf';
  import html2canvas from 'html2canvas';
  // import { getCurrentInstance } from 'vue';
   
  function oo() {
  console.log('你好');
  // date = data.value.data
  // console.log(date);
  console.log(tyfx.value);
}

let tyfx = ref()

// const dele = () => {
//       // 发送 POST 请求到后端删除接口
//       axios.post('http://127.0.0.1:8000/delete', { id: 2 })
//         .then(response => {
//           // 处理成功响应
//           console.log(response.data);
//         })
//         .catch(error => {
//           // 处理错误
//           console.error(error);
//         });

const dele = (record) => {
  axios({
	method: 'post',
	url: 'http://127.0.0.1:8000/delete',
  headers: {
      'Content-Type': 'application/x-www-form-urlencoded'
    },
    data: new URLSearchParams({
      id: record.id
    })
})
  .then(response => {console.log(response.data); console.log(record.id); })
  .catch(error => {console.error(error); console.log(record.id);});
}

  const exportToPDF = () => {
    html2canvas(tyfx.value).then(_d => {
      let imgUrlData = _d.toDataURL("image/jpeg",1.0)
      const pdfDoc = new jsPDF('','pt','a4')
      pdfDoc.addImage(imgUrlData,'jpeg',0,0,600,300)
      pdfDoc.save('个人信息.pdf')
    }) }

  const showDrawer = (record) =>{
    shuju.ID_card = record.ID_card;
    shuju.Sno = record.Sno ;
    shuju.before_class = record.before_class ;
    shuju.before_teacher = record.before_teacher ;
    shuju.birthday = record.birthday ;
    shuju.domicile = record.domicile ;
    shuju.duties = record.duties ;
    shuju.enlist_place = record.enlist_place ;
    shuju.enlist_time = record.enlist_time ;
    shuju.family_number = record.family_number ;
    shuju.gender = record.gender ;
    shuju.id = record.id ;
    shuju.isValid = record.isValid ;
    shuju.name = record.name ;
    shuju.nation = record.nation ;
    shuju.number = record.number ;
    shuju.pend = decodeURIComponent(record.pend) ;
    shuju.politic = record.politic ;
    shuju.retire_class = record.retire_class ;
    shuju.retire_teacher = record.retire_teacher ;
    shuju.retire_time = record.retire_time ;
    shuju.rewards = decodeURIComponent(record.rewards) ;
    shuju.searvice_troops = record.searvice_troops ;
    shuju.sign_photo = record.sign_photo ;
    shuju.personal_photo = record.personal_photo ;
    shuju.certifiate = record.certifiate ;
    shuju.enlist_photo = record.enlist_photo ;
    shuju.retire_photo = record.retire_photo ;
    open.value = true;
  };

  const shuchu = (record) => {
  console.log(record); 
};
 let shuju = reactive({
  ID_card: "",
  Sno: "",
  before_class: "",
  before_teacher: "",
  birthday: "",
  domicile:  "",
  duties:  "",
  enlist_place:  "",
  enlist_time:  "",
  family_number:  "",
  gender:  "",
  id:  "",
  isValid: true,
  name:  "",
  nation:  "",
  number:   "",
  pend:  "",
  politic:  "",
  retire_class:  "",
  retire_teacher:  "",
  retire_time:  "",
  rewards:  "",
  searvice_troops:  "",

  sign_photo:  "",
  personal_photo:  "",
  certifiate:  "",
  enlist_photo:  "",
  retire_photo:  "",
 })

 

const onClose = () => {
  open.value = false;
};


  
  onMounted(() => {
  axios.get('http://localhost:8000/query')
    .then(response => {
      console.log(response.data.data);
      console.log("这个是一手数据代码");
      Object.assign(date,response.data.data)
      console.log(date);
    })
    .catch(error => {
      console.error(error);
    });
  console.log("相应函数");
});


  const columns: TableColumnsType = [
    { title: 'id', width: 50, dataIndex: 'id', key: 'name', fixed: 'left' },
    { title: '姓名', width: 80, dataIndex: 'name', key: 'age', fixed: 'left' },
    { title: 'id', dataIndex: 'id', key: '1', width: 150 },
    { title: '姓名', dataIndex: 'name', key: '2', width: 150 },
    { title: '性别', dataIndex: 'gender', key: '3', width: 150 },
    { title: '民族', dataIndex: 'nation', key: '4', width: 150 },
    { title: '出生日期', dataIndex: 'birthday', key: '5', width: 150 },
    { title: '政治面貌', dataIndex: 'politic', key: '6', width: 150 },
    { title: '学号', dataIndex: 'Sno', key: '7', width: 150 },
    { title: '户籍地', dataIndex: 'domicile', key: '8' },
    { title: '身份证号', dataIndex: 'ID_card', key: '9' },
    { title: '入伍时间', dataIndex: 'enlist_time', key: '10' },
    { title: '退役时间', dataIndex: 'retire_time', key: '11' },
    { title: '入伍前班导师', dataIndex: 'before_teacher', key: '12' },
    { title: '退伍后班导师', dataIndex: 'retire_teacher', key: '13' },
    { title: '入伍前学院班级', dataIndex: 'before_class', key: '14' },
    { title: '退伍后学院班级', dataIndex: 'retire_class', key: '15' },
    { title: '服役部队', dataIndex: 'searvice_troops', key: '16' },
    { title: '职务', dataIndex: 'duties', key: '17' },
    { title: '本人电话', dataIndex: 'number', key: '18' },
    { title: '家庭电话', dataIndex: 'family_number', key: '19' },
    { title: '入伍地', dataIndex: 'enlist_place', key: '20' },
    { title: '挂科科目', dataIndex: 'pend', key: 'lm' },
    { title: '奖惩情况', dataIndex: 'rewards', key: 'lm' },
    { title: '专业培训及证书', dataIndex: 'certifiate', key: 'base64' },
    { title: '个人照', dataIndex: 'personal_photo', key: 'base64' },
    { title: '入伍通知书', dataIndex: 'enlist_photo', key: 'base64' },
    { title: '退役证', dataIndex: 'retire_photo', key: 'base64' },
    { title: '本人签字', dataIndex: 'sign_photo', key: 'base64' },
    {
      title: '调整',
      key: 'operation',
      fixed: 'right',
      width: 100,
    },
  ];
  const form = reactive({
  name: '',
  url: '',
  owner: '',
  type: '',
  approver: '',
  dateTime: null,
  description: '',
});
  
  interface DataItem {
    key: number;
    name: string;
    age: number;
    address: string;
  } 
    let date = reactive([]);




const open = ref<boolean>(false);



</script>
<style scoped>
:deep(.my-label) {
  background: var(--el-color-success-light-9) !important;
}
:deep(.my-content) {
  background: var(--el-color-danger-light-9);
}
</style>
<!-- 
// 假设数据结构与你定义的假数据结构相同 const是常量 不可变
// const date = ref([]);
// let data = reactive([
// {
//           "id": 1, //id
//           "name": "李博", //name
//           "gender": "3",
//           "nation": "1",
//           "birthday": "2024-03-13",
//           "politic": "1",
//           "Sno": "1",
//           "domicile": "1",
//           "ID_card": "1",
//           "enlist_time": "2024-03-13",
//           "retire_time": "2024-03-27",
//           "before_teacher": "1",
//           "retire_teacher": "1",
//           "before_class": "1",
//           "retire_class": "1",
//           "searvice_troops": "11",
//           "duties": "11",
//           "number": "1",
//           "family_number": "11",
//           "enlist_place": "1",
//           "pend": "11",
//           "rewards": "11",
//           "certifiate": "0",
//           "personal_photo": "1",
//           "enlist_photo": "1",
//           "retire_photo": "1",
//           "sign_photo": "1",
//           "isValid": true
//       },{
//           "id": 1, //id
//           "name": "李博", //name
//           "gender": "3",
//           "nation": "1",
//           "birthday": "2024-03-13",
//           "politic": "1",
//           "Sno": "1",
//           "domicile": "1",
//           "ID_card": "1",
//           "enlist_time": "2024-03-13",
//           "retire_time": "2024-03-27",
//           "before_teacher": "1",
//           "retire_teacher": "1",
//           "before_class": "1",
//           "retire_class": "1",
//           "searvice_troops": "11",
//           "duties": "11",
//           "number": "1",
//           "family_number": "11",
//           "enlist_place": "1",
//           "pend": "11",
//           "rewards": "11",
//           "certifiate": "0",
//           "personal_photo": "1",
//           "enlist_photo": "1",
//           "retire_photo": "1",
//           "sign_photo": "1",
//           "isValid": true
//       },{
//           "id": 2, //id
//           "name": "热热热热热热", //name
//           "gender": "3",
//           "nation": "1",
//           "birthday": "2024-03-13",
//           "politic": "1",
//           "Sno": "1",
//           "domicile": "1",
//           "ID_card": "1",
//           "enlist_time": "2024-03-13",
//           "retire_time": "2024-03-27",
//           "before_teacher": "1",
//           "retire_teacher": "1",
//           "before_class": "1",
//           "retire_class": "1",
//           "searvice_troops": "11",
//           "duties": "11",
//           "number": "1",
//           "family_number": "11",
//           "enlist_place": "1",
//           "pend": "11",
//           "rewards": "11",
//           "certifiate": "0",
//           "personal_photo": "1",
//           "enlist_photo": "1",
//           "retire_photo": "1",
//           "sign_photo": "1",
//           "isValid": true
//       }]); -->
  


<!-- <a-form :model="form"  layout="vertical">
  <a-row :gutter="16">
    <a-col :span="12">
      <a-form-item label="Name" name="name">
        <a-input v-model:value="form.name" placeholder="Please enter user name" />
      </a-form-item>
    </a-col>
    <a-col :span="12">
      <a-form-item label="Url" name="url">
        <a-input
          v-model:value="form.url"
          style="width: 100%"
          addon-before="http://"
          addon-after=".com"
          placeholder="please enter url"
        />
      </a-form-item>
    </a-col>
  </a-row>
  <a-row :gutter="16">
    <a-col :span="12">
      <a-form-item label="Owner" name="owner">
        <a-select v-model:value="form.owner" placeholder="Please a-s an owner">
          <a-select-option value="xiao">Xiaoxiao Fu</a-select-option>
          <a-select-option value="mao">Maomao Zhou</a-select-option>
        </a-select>
      </a-form-item>
    </a-col>
    <a-col :span="12">
      <a-form-item label="Type" name="type">
        <a-select v-model:value="form.type" placeholder="Please choose the type">
          <a-select-option value="private">Private</a-select-option>
          <a-select-option value="public">Public</a-select-option>
        </a-select>
      </a-form-item>
    </a-col>
  </a-row>
  <a-row :gutter="16">
    <a-col :span="12">
      <a-form-item label="Approver" name="approver">
        <a-select v-model:value="form.approver" placeholder="Please choose the approver">
          <a-select-option value="jack">Jack Ma</a-select-option>
          <a-select-option value="tom">Tom Liu</a-select-option>
        </a-select>
      </a-form-item>
    </a-col>
    <a-col :span="12">
      <a-form-item label="DateTime" name="dateTime">
        <a-date-picker
          v-model:value="form.dateTime"
          style="width: 100%"
          :get-popup-container="trigger => trigger.parentElement"
        />
      </a-form-item>
    </a-col>
  </a-row>
  <a-row :gutter="16">
    <a-col :span="24">
      <a-form-item label="Description" name="description">
        <a-textarea
          v-model:value="form.description"
          :rows="4"
          placeholder="please enter url description"
        />
      </a-form-item>
    </a-col>
  </a-row>
</a-form> -->