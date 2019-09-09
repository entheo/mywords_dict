// pages/cards/cards.js
const app = getApp()
Page({

  /**
   * 页面的初始数据
   */
  data: {
    i:0,
    template:'test'
  },


  audioPlay: function (e) {
    console.log(e)
    this.setData({
      accent: e.target.dataset.accent
    })
    console.log(this.data.accent)
    this.audioCtx.play()
  },

  touchStart(e) {
    this.setData({
      start_x: e.changedTouches[0].clientX,
      start_y: e.changedTouches[0].clientY,
    })

    console.log('开始', this.data.start_x)
  },

  touchEnd(e) {
    var end_x = e.changedTouches[0].clientX
    var end_y = e.changedTouches[0].clientY
    var x = end_x - this.data.start_x
    var y = end_y - this.data.start_y
    console.log('结束', end_x, x)
    //右滑查看上一个
    if (x > 50) {
      console.log('右滑',x)
      var index = this.data.i-1
      console.log(index)
      if(this.data.i>0){
        this.setData({
          i:index
        })
      }
    }
    // 左滑查看下一个
    else if (x < -50) {
      console.log('左滑',x)
      var index = this.data.i + 1
      if (index<this.data.length) {
        this.setData({
          i: index
        })}
    }
    // 上滑查看翻译
    else if(y < -40){
      console.log('上滑',y)
      this.setData({
        template:'trans'
      })
    }

    // 下滑隐藏翻译
    else if(y > 50){
      console.log('下滑',y)
      this.setData({
        template:'test'
      })
    }

  },

  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {
   this.setData({
     memo_dict:JSON.parse(app.globalData.memo_dict),
     length:JSON.parse(app.globalData.memo_dict).length
   })
  },

  /**
   * 生命周期函数--监听页面初次渲染完成
   */
  onReady: function () {
    this.audioCtx = wx.createAudioContext('pronunciation')
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