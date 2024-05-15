var comm = {};
comm.getAdv = new (function () {
  this.fetchBanners = function (that,category,api) {
    //1：充值 2：消费  3 结算  4 分享  5 会员卡信息
    var requestUrl = {
      moduleName: 'Home',
      controllerName: 'CommApi',
      methodName: 'getAdvPic'
    };
    var inputParaJson = {
      category: category
    };

    var callback = function (data) {
      if (data.result != 0) {
        let searchList = data.result;
        that.setData({
          banners: searchList, //获取数据数组  
        });
       //console.log(that.data.banners);
      }
    }
    api.net.doRequest(requestUrl, inputParaJson, callback);
  };  
  this.fetchAdvById = function (that, autoid, api) {
    var requestUrl = {
      moduleName: 'Home',
      controllerName: 'CommApi',
      methodName: 'getAdvContentById'
    };
    var inputParaJson = {
      autoid: autoid
    };

    var callback = function (data) {

      if (data.result != 0) {
        let searchList = data.result[0];
        that.setData({
          title: searchList.title,
          add_time: searchList.add_time,
          content: searchList.content
        });
      }
    }
    api.net.doRequest(requestUrl, inputParaJson, callback);
  };
  this.gotowebpage = function (event) {
    var autoid = event.target.dataset.id;
    wx.navigateTo({
      url: '../webpage/webpage?autoid=' + autoid
    })
  };
})();
module.exports = comm;
