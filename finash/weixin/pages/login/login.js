// pages/logino/logino.js
const app = getApp();
Page({

  data: {
    // json: '',
    inputSno :'',
    ID_card:'',
    ID_card_S:'',
    // studentId: '',
    // password: '',
    // passwordd: '',
    json: '',
  },

  login: function () {
    // 检查 inputSno 和 ID_card_S 是否都有值
    if (!this.data.inputSno || !this.data.ID_card_S) {
      // 如果有一方为空，弹窗提示填写错误
      wx.showToast({
        title: '请填写学号和身份证',
        icon: 'none',
        duration: 2000
      });
      return;
    }
  
    // 在 json 数据中查找与 inputSno 相匹配的学生信息
    const matchedStudent = this.data.json.data.find(student => student.Sno === this.data.inputSno);
  
    if (matchedStudent) {
      // 找到了匹配的学生信息，检查 ID_card_S 是否与匹配的学生的 ID_card 相同
      if (this.data.ID_card_S === matchedStudent.ID_card) {
        getApp().globalData.ID_card_S = this.data.ID_card_S;
        // 密码匹配，执行导航
        wx.navigateTo({
          url: '/pages/check/check',
        });
        // 设置全局数据
        app.globalData.ID_card_S = this.data.ID_card_S;
      } else {
        // 密码不匹配，弹窗提示重新输入密码
        wx.showToast({
          title: '身份证错误，请重新输入',
          icon: 'none',
          duration: 2000
        });
      }
    } else {
      // 没找到匹配的学生信息，弹窗提示输入错误
      wx.showToast({
        title: '学号不存在，请重新输入',
        icon: 'none',
        duration: 2000
      });
    }
  },
  printJson: function () {
    console.log('当前 JSON 数据:', this.data);
  },
  getpass: function (e) {
    this.setData({
      ID_card_S: e.detail.value
    });
  },
  getnum: function (e) {
    this.setData({
      inputSno: e.detail.value
    });
  },
  // getnum: function (e) {
  //   const inputSno = e.detail.value;
  //   for (let i = 0; i < this.data.json.data.length; i++) {
  //     if (this.data.json.data[i].Sno === inputSno) {
  //       console.log(this.data.json.data[i].ID_card);
  //       this.setData({
  //         ID_card_S: this.data.json.data[i].ID_card
  //       });
  //       break;  // 匹配到就跳出循环
  //     }
  //   }
  // },
// ///////////////////////////////////////////////////////////////////////////////////
// getnum: function (e) {
//   const SnoInput = e.detail.value;

//   // 发起请求
//   this.getDataFromServer()
//     .then((json) => {
//       // 在请求完成后执行匹配逻辑
//       this.setData({
//         json: json
//       });

//       for (let i = 0; i < this.data.json.length; i++) {
//         if (this.data.json[i].Sno === SnoInput) {
//           console.log(this.data.json[i].ID_card)
//           this.setData({
//             ID_card_S: this.data.json[i].ID_card
//           });
//           break;  // 匹配到就跳出循环
//         }
//       }
//     })
//     .catch((error) => {
//       console.error('请求失败', error);
//     });
// },

// 封装请求为 Promise
// getDataFromServer: function () {
//   return new Promise((resolve, reject) => {
//     wx.request({
//       url: 'http://127.0.0.1:8000/query',
//       method: 'GET',
//       success: (res) => {
//         resolve(res.data.data); // 假设数据在 res.data.data 中
//       },
//       fail: (res) => {
//         reject(res);
//       }
//     });
//   });
// },
////////////////////////////////////////////////////////////////////////////

  onLoad(options) {
    wx.request({
      url: 'http://127.0.0.1:8000/query',
      method: 'GET', // 这里使用 GET 方法，你可以根据实际需求选择其他方法
      // json : this.res.data,
      success: (res) => {
        // 将获取到的数据保存到data中的json变量中
        this.setData({
          json: res.data
        });
        console.log('请求成功', this.data.json);
      },
      fail: function (res) {
        console.log('请求失败', res);
      }
    });
  },
})