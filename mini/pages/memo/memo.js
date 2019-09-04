// pages/memo/memo.js
const app = getApp()
Page({

  /**
   * 页面的初始数据
   */
  data: {
    list: app.globalData.list
  },

  /*tabChange(e) {
    app.change(e)
  },*/

  getMemo:function(openid){
    var that = this
    wx.request({
      url : app.globalData.host+'/memo/find',
      method : 'POST',
      data:{
        open_id:openid
      },
      success(res){
        console.log(res)
        that.setData({
          words:res.data.words
        })
        
      }
      
    })
  },

  toSearch(e){
    console.log(e)
    wx.navigateTo({
      url: '/pages/result/result?word=' + e.target.dataset.word
    })
  },


  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {
    app.getToken().then(res=>{
      this.getMemo(wx.getStorageSync('open_id'))
    })
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
    app.getToken().then(res => {
      this.getMemo(wx.getStorageSync('open_id'))
    })

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