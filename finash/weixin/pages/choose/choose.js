// var app = getApp()
Page({
  data: {
    a1src:'../../images/icon_添加.png',
    a2src: '../../images/查找图标.png',
    a3src: '../../images/学校.png',
    a4src:  '../../images/军队.png',
    signupimg:'../../images/1.jpg',
    imgsrc:'../../images/zx2.jpg',
    imgsrc3:'../../images/zx3.jpg',
    imgsrc4:'../../images/zx4.jpg',
    imgsrc5:'../../images/zx5.jpg',
    // iconsrc:'../../image/usercount.png',
    // jtsrc:'../../image/icon-jt.png',
    imgUrls: [
      '../../images/l1.jpg',
      '../../images/l2.jpg',
      '../../images/l3.jpg',
    ],
    indicatorDots: true,
    autoplay: true,
    interval: 5000,
    duration: 1000 
  },
  goto: function () {
    wx.navigateTo({
      url: '/pages/up/up',
    });
  },
  gotoup: function () {
    wx.navigateTo({
      url: '/pages/up/up',
    });
    console.log('6')
  },
  gotocheck: function () {
    wx.navigateTo({
      url: '/pages/login/login',
    });
    console.log('1')
  },
  gotozb: function () {
    wx.navigateTo({
      url: "/pages/zb/zb",
    });
    console.log('2')
  },
  gotozx1: function () {
    wx.navigateTo({
      url: "/pages/zx1/zx1",
    });
    console.log('3')
  },
  gotozx2: function () {
    wx.navigateTo({
      url: "/pages/zx2/zx2",
    });
    console.log('4')
  },
  gotozx3: function () {
    wx.navigateTo({
      url: "/pages/zx3/zx3",
    });
    console.log('5')
  }
})
