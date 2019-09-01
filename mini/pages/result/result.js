// pages/result/result.js
const app = getApp()


Page({

  /**
   * 页面的初始数据
   */
  data: {
    word_memo:''

  },

toSearch(e){
    this.getTrans(e.detail.value.word)
    console.log(e)
} , 

//查询单词
  getTrans: function (word) {
    console.log(word)
    var that = this
    wx.request({
      url: app.globalData.host + '/dict/',
      method: 'GET',
      data: {
        word: word
      },
      success(res) {
        console.log(res.data)
        that.setData({
          trans: res.data.res,
          word_memo:word,
          word:word
        })
        console.log(res.data.res)
      }
    })
  },

addMemo:function(word){
  console.log(word)
  console.log('openid',wx.getStorageSync('open_id'))

  wx.request({
    url: app.globalData.host + '/memo/add',
    method: 'POST',
    data: {
      word: word,
      open_id: wx.getStorageSync('open_id'),
    },
    success(res) {
      console.log(res)
    }
  })
},

//添加进生词本
toAddMemo(e){
    app.getToken().then(res => {
      console.log(res)
      this.addMemo(this.data.word_memo)
    })
},

//查看生词本
toMemo:function(){
  wx.navigateTo({
    url: '/pages/memo/memo',
  })
},
  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {
    this.setData({
      word:options.word,
    })
    this.getTrans(options.word)
  },



  /**
   * 生命周期函数--监听页面初次渲染完成
   */
  onReady: function () {

  },

  /**
   * 生命周期函数--监听页面显示
   */
  onShow: function () {

  },

  /**
   * 生命周期函数--监听页面隐藏
   */
  onHide: function () {

  },

  /**
   * 生命周期函数--监听页面卸载
   */
  onUnload: function () {
    
  },

  /**
   * 页面相关事件处理函数--监听用户下拉动作
   */
  onPullDownRefresh: function () {

  },

  /**
   * 页面上拉触底事件的处理函数
   */
  onReachBottom: function () {

  },

  /**
   * 用户点击右上角分享
   */
  onShareAppMessage: function () {

  }
})