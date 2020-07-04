// pages/memo/memo.js
const app = getApp()
var start_x,start_y
var memo = require('../../utils/memo.js')
Page({

  /**
   * 页面的初始数据
   */
  data: {
    list: app.globalData.list,
    template:'welcom'
  },

  /*tabChange(e) {
    app.change(e)
  },*/

  getMemoList:function(openid){
    var that = this
    wx.request({
      url : app.globalData.host+'/memo/find',
      method : 'POST',
      data:{
        open_id:openid
      },
      success(res){
        console.log(res.data)
        app.globalData.memo_list=res.data.words
        that.setData({
          words:app.globalData.memo_list,
          num:app.globalData.memo_list.length
        })
        if (res.data.words){
          that.setData({
            template:'active'
          })
        }
      }
    })
  },

  //获取用户的生词字典
  getMemoDict: function (openid) {
    var that = this
    wx.request({
      url: app.globalData.host + '/memo/get_user_memo_dict',
      method: 'POST',
      data: {
        open_id: openid
      },
      success(res) {
        console.log(res)
        app.globalData.memo_dict = JSON.stringify(res.data.dict)
        /*that.setData({
          dict: res.data.dict
        })*/
      }
    })
  },
 

  toSearch(e){
    console.log(e)
    wx.navigateTo({
      url: '/pages/result/result?word=' + e.target.dataset.word
    })
  },

  toWordList(e){
    console.log(e)
    if(e.currentTarget.dataset.name){
      wx.navigateTo({
        url: '/pages/word-list/word-list?name='+e.currentTarget.dataset.name,
      })
    }
    else{
      wx.navigateTo({
        url: '/pages/word-list/word-list?words=' + JSON.stringify(app.globalData.memo_list),
      })
    }
  },

  toCards(){
    if(this.data.words){
      wx.navigateTo({
        url: '/pages/cards/cards'
      })
    }
    else{
      wx.showToast({
        title: '请从字典查询中添加单词',
        icon:'none',
        duration:2000
      })
    }

    },



  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {
    console.log('load')
    app.getToken()
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
      var that = this
      memo.getMemoDict(wx.getStorageSync('open_id'), that).then(res => {
        that.setData({
          dict: res.data.dict
        })
      })
      this.getMemoList(wx.getStorageSync('open_id'))

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