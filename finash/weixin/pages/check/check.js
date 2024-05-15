// pages/check/check.js
const app = getApp();
Page({
  data: {
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
    gender: '',
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
    ID_card_S: app.globalData.ID_card_S,
    json: '',
  },
  printJson: function () {
    console.log('当前 JSON 数据:', this.data);
  },
  // onLoad(options) {
  //   wx.request({
  //     url: 'http://127.0.0.1:8000/query',
  //     method: 'GET', // 这里使用 GET 方法，你可以根据实际需求选择其他方法
  //     // json : this.res.data,
  //     success: (res) => {
  //       // 将获取到的数据保存到data中的json变量中
  //       this.setData({
  //         json: res.data
  //       });
  //       console.log('请求成功', this.data.json);
  //     },
  //     fail: function (res) {
  //       console.log('请求失败', res);
  //     }
  //   });
  // },
  onLoad(options) {
    wx.request({
      url: 'http://127.0.0.1:8000/query',
      method: 'GET',
      success: (res) => {
        // 将获取到的数据保存到 data 中的 json 变量中
        this.setData({
          json: res.data
        });
  
        // 匹配 ID_card_S
        const matchedStudent = this.data.json.data.find(student => student.ID_card === this.data.ID_card_S);
  
        if (matchedStudent) {
          // 将匹配到的数据分别赋值给对应字段
          this.setData({
            ID_card: matchedStudent.ID_card,
            name: matchedStudent.name,
            nation: matchedStudent.nation,
            politic: matchedStudent.politic,
            Sno: matchedStudent.Sno,
            domicile:  matchedStudent.domicile,
            before_teacher: matchedStudent.before_teacher,
            retire_teacher: matchedStudent.retire_teacher,
            before_class: matchedStudent.before_class,
            retire_class: matchedStudent.retire_class,
            searvice_troops: matchedStudent.searvice_troops,
            duties: matchedStudent.duties,
            number:  matchedStudent.number,
            family_number: matchedStudent.family_number,
            enlist_place: matchedStudent.enlist_place,
            gender: matchedStudent.gender,
            birthday: matchedStudent.birthday,
            enlist_time: matchedStudent.enlist_time,
            retire_time: matchedStudent.retire_time,
            personal_photo: matchedStudent.personal_photo,
            enlist_photo: matchedStudent.enlist_photo,
            retire_photo: matchedStudent.retire_photo,
            sign_photo: matchedStudent.sign_photo,
            pend: matchedStudent.pend,
            rewards: matchedStudent.rewards,
            certifiate: matchedStudent.certifiate,
          });
  
          // 打印匹配到的数据
          console.log('匹配到的数据:', matchedStudent);
        } else {
          console.log('未匹配到相应的数据');
        }
  
        console.log('请求成功', this.data.json);
      },
      fail: function (res) {
        console.log('请求失败', res);
      }
    });
  },





goto: function () {
  wx.navigateTo({
    url: '/pages/up/up',
  });
},


})