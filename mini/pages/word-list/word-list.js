// pages/word-list/word-list.js
var app = getApp()
Page({

  /**
   * 页面的初始数据
   */
  data: {

  },

  toSearch(e){
    wx.navigateTo({
      url: '/pages/result/result?word='+e.target.dataset.word,
    })

  },

  deleteWord(e){
    var word = e.currentTarget.dataset.word
    var that = this

    wx.showModal({
      title:'提示',
      content:'确实删除这个生词么？',
      success(res){
        if(res.confirm){
          wx.request({
            method:'POST',
            url: app.globalData.host+'/memo/delete_memo_word',
            data: {
              word: word,
              open_id: wx.getStorageSync('open_id'),
            },
            success(res){
              console.log(res.data)
              if(res.data.status){
                app.globalData.memo_list=res.data.words
                that.setData({
                  word_list:app.globalData.memo_list
                })
              }
            }
          })
        }
        else if(res.cancel){
          console.log('用户放弃删除')
        }
      }
    })

   

  },

  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {
    //修改title
    wx.setNavigationBarTitle({
      title: options.name  
    })
    console.log(options)
    if(options.words){
      this.setData({
        word_list: JSON.parse(options.words)
      })
    }
    else if(options.name){
      var that = this
      wx.request({
        url: app.globalData.host+'/word_list/get_word_list',
        method:'POST',
        data:{
          name:options.name
        },
        success(res){
          that.setData({
            word_list: res.data.word_list
          })
        }
      })
    }
   
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