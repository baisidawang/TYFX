// var util = require('../../utils/util.js')
// const app = getApp();
// var api = app.api;

Page({
  dd: [],
  data: {
    genderArray: ['男', '女'], // 可选的性别数组
    fieldx: [
      { name: 'pend', type: 'date', bindInput: 'getpend', chineseName: '挂科科目' },
      { name: 'rewards', type: 'date', bindInput: 'getrewards', chineseName: '奖惩情况' },
    ],
    fields: [
      { name: 'name', type: 'date', bindInput: 'getname', chineseName: '姓名' },
      { name: 'nation', type: 'date', bindInput: 'getnation', chineseName: '民族' },
      { name: 'politic', type: 'date', bindInput: 'getpolitic', chineseName: '政治面貌' },
      { name: 'Sno', type: 'date', bindInput: 'getSno', chineseName: '学号' },
      { name: 'domicile', type: 'date', bindInput: 'getdomicile', chineseName: '户籍地' },
      { name: 'ID_card', type: 'date', bindInput: 'getID_card', chineseName: '身份证号' },
      { name: 'before_teacher', type: 'date', bindInput: 'getbefore_teacher', chineseName: '入伍前班导师' },
      { name: 'retire_teacher', type: 'date', bindInput: 'getretire_teacher', chineseName: '退伍后班导师' },
      { name: 'before_class', type: 'date', bindInput: 'getbefore_class', chineseName: '入伍前学院班级' },
      { name: 'retire_class', type: 'date', bindInput: 'getretire_class', chineseName: '退伍后学院班级' },
      { name: 'searvice_troops', type: 'date', bindInput: 'getsearvice_troops', chineseName: '服役部队' },
      { name: 'duties', type: 'date', bindInput: 'getduties', chineseName: '职务' },
      { name: 'number', type: 'date', bindInput: 'getnumber', chineseName: '本人电话' },
      { name: 'family_number', type: 'date', bindInput: 'getfamily_number', chineseName: '家庭电话' },
      { name: 'enlist_place', type: 'date', bindInput: 'getenlist_place', chineseName: '入伍地' },
    ],
    name: '',
    nation: '',
    politic: '',
    Sno: '',
    domicile: '',
    ID_card: '',
    before_teacher: '',
    retire_teacher: '',
    before_class: '',
    retire_class: '',
    searvice_troops: '',
    duties: '',
    number: '',
    family_number: '',
    enlist_place: '',
    gender: '请选择性别', // 默认显示的文本
    birthday: '',
    enlist_time: '',
    retire_time: '',
    personal_photo: '',
    enlist_photo: '',
    retire_photo: '',
    sign_photo: '',

    pend: '',
    rewards: '',
    certifiate: '',
  },
  formSubmit(e) {
    e.detail.value.personal_photo = this.data.personal_photo;
    e.detail.value.enlist_photo = this.data.enlist_photo;
    e.detail.value.retire_photo = this.data.retire_photo;
    e.detail.value.sign_photo = this.data.sign_photo;
    e.detail.value.certifiate = this.data.certifiate;
    console.log('form发生了submit事件，携带数据为：', e.detail.value)
    wx.request({
      url: 'http://127.0.0.1:8000/adds',
      method: 'POST',
      data: e.detail.value,
      success: function (res) {
        console.log(res.data);
      },
      fail: function (res) {
        console.log('fail');
      }
    });
  },

  submitForm: function (e) {
    console.log('form发生了submit事件，携带数据为：', e.detail.value)
    e.detail.value.personal_photo = this.data.personal_photo;
    e.detail.value.enlist_photo = this.data.enlist_photo;
    e.detail.value.retire_photo = this.data.retire_photo;
    e.detail.value.sign_photo = this.data.sign_photo;
    e.detail.value.certifiate = this.data.certifiate;
    wx.request({
      url: 'http://127.0.0.1:8000/add',
      method: 'POST',
      data: e.detail.value,
      success: function (res) {
        console.log(res.data);
      },
      fail: function (res) {
        console.log('fail');
      }
    });
  },







  uploadp() {
    wx.chooseMedia({
      count: 1,
      mediaType: ['image'],
      sourceType: ['album', 'camera'],
      success: (res) => {
        const tempFilePath = res.tempFiles[0].tempFilePath;
        const fileSize = res.tempFiles[0].size;
        console.log(tempFilePath);
        console.log(fileSize);
        
        // 将选择的照片路径保存到data中
        this.setData({
          personal_photo: tempFilePath
        });
        // 上传照片的逻辑
        // 这里可以调用你的上传图片的接口，并根据返回的结果进行处理
      }
    })
  },
  uploade() {
    wx.chooseMedia({
      count: 1,
      mediaType: ['image'],
      sourceType: ['album', 'camera'],
      success: (res) => {
        const tempFilePath = res.tempFiles[0].tempFilePath;
        const fileSize = res.tempFiles[0].size;
        console.log(tempFilePath);
        console.log(fileSize);
        
        // 将选择的照片路径保存到data中
        this.setData({
          enlist_photo: tempFilePath
        });
        // 上传照片的逻辑
        // 这里可以调用你的上传图片的接口，并根据返回的结果进行处理
      }
    })
  },
  uploadr() {
    wx.chooseMedia({
      count: 1,
      mediaType: ['image'],
      sourceType: ['album', 'camera'],
      success: (res) => {
        const tempFilePath = res.tempFiles[0].tempFilePath;
        const fileSize = res.tempFiles[0].size;
        console.log(tempFilePath);
        console.log(fileSize);
        
        // 将选择的照片路径保存到data中
        this.setData({
          retire_photo: tempFilePath
        });
        // 上传照片的逻辑
        // 这里可以调用你的上传图片的接口，并根据返回的结果进行处理
      }
    })
  },
  uploads() {
    wx.chooseMedia({
      count: 1,
      mediaType: ['image'],
      sourceType: ['album', 'camera'],
      success: (res) => {
        const tempFilePath = res.tempFiles[0].tempFilePath;
        const fileSize = res.tempFiles[0].size;
        console.log(tempFilePath);
        console.log(fileSize);
        
        // 将选择的照片路径保存到data中
        this.setData({
          sign_photo: tempFilePath
        });
        // 上传照片的逻辑
        // 这里可以调用你的上传图片的接口，并根据返回的结果进行处理
      }
    })
  },
  uploadc() {
    wx.chooseMedia({
      count: 1,
      mediaType: ['image'],
      sourceType: ['album', 'camera'],
      success: (res) => {
        const tempFilePath = res.tempFiles[0].tempFilePath;
        const fileSize = res.tempFiles[0].size;
        console.log(tempFilePath);
        console.log(fileSize);
        
        // 将选择的照片路径保存到data中
        this.setData({
          certifiate: tempFilePath
        });
        // 上传照片的逻辑
        // 这里可以调用你的上传图片的接口，并根据返回的结果进行处理
      }
    })
  },
 
 







  bindGenderChange: function (e) {
    const index = e.detail.value;
    const gender = this.data.genderArray[index];
    console.log('选择的性别为', gender);
    this.setData({
      gender: gender,
    });
  },

  bindDateChange: function (e) {
    this.setData({
      birthday: e.detail.value
    })
  },
  bindDateChangeru: function (e) {
    this.setData({
      enlist_time: e.detail.value
    })
  },
  bindDateChangetui: function (e) {
    this.setData({
      retire_time: e.detail.value
    })
  },
  






  getname(e) {
    this.setData({
      name: e.detail.value
    });
  },
  getnation(e) {
    this.setData({
      nation: e.detail.value
    });
  },
  getpolitic(e) {
    this.setData({
      politic: e.detail.value
    });
  },
  getSno(e) {
    this.setData({
      Sno: e.detail.value
    });
  },
  getdomicile(e) {
    this.setData({
      domicile: e.detail.value
    });
  },
  getID_card(e) {
    this.setData({
      ID_card: e.detail.value
    });
  },
  getbefore_teacher(e) {
    this.setData({
      before_teacher: e.detail.value
    });
  },
  getretire_teacher(e) {
    this.setData({
      retire_teacher : e.detail.value
    });
  },
  getbefore_class(e) {
    this.setData({
     before_class: e.detail.value
    });
  },
  getretire_class(e) {
    this.setData({
      retire_class: e.detail.value
    });
  },
  getsearvice_troops(e) {
    this.setData({
      searvice_troops: e.detail.value
    });
  },
  getduties(e) {
    this.setData({
      duties: e.detail.value
    });
  },
  getnumber(e) {
    this.setData({
      number: e.detail.value
    });
  },
  getfamily_number(e) {
    this.setData({
      family_number: e.detail.value
    });
  },
  getenlist_place(e) {
    this.setData({
      enlist_place: e.detail.value
    });
  },
  getpend(e) {
    this.setData({
      pend : e.detail.value
    });
  },  
  getrewards(e) {
    this.setData({
      rewards: e.detail.value
    });
  },
  getcertifiate(e) {
    this.setData({
      certifiate: e.detail.value
    });
  },

})
