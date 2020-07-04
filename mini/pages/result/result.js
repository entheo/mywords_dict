// pages/result/result.js
const app = getApp()


Page({

  /**
   * 页面的初始数据
   */
  data: {
    word_memo:'',
  },

toSearch(e){
    console.log(e)
    this.getTrans(e.detail.value.word)    
} , 

checkToSearch(e){
  if(this.data.en==null){
    wx.navigateTo({
      url: '/pages/result/result?word='+e.target.dataset.word,
    })
  }
},

toConfirmSearch(e){
    this.setData({
      
    })
    this.getTrans(e.detail.value)
},

toClear(e){
  this.setData({
    word:'',
    focus:true
  })
},

  audioPlay: function (e) {
    this.setData({
      accent:e.target.dataset.accent
    })
    console.log(this.data.accent)
    this.audioCtx.play()
  },


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
        console.log(res.data.res)
        that.setData({
          trans: res.data.res.trans,
          sentences:res.data.res.sentences,
          word: word,
          en:null,
          link:'link',
          show:true
        })
        if(res.data.res.language=='en'){
          that.setData({
            pron_us: res.data.res.pronounce.us,
            pron_uk: res.data.res.pronounce.uk,
            word_memo: word,
            en:true,
            link:''
          })
        } 
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
      console.log(res.data)
      if (res.data.res.status) {
        wx.showToast({
          title: '添加至生词本',
        })}
      else{
        wx.showToast({
          icon:'none',
          title: '生词本中已有',
        })
        }
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
    let windowHeight = wx.getSystemInfoSync().windowHeight 
    console.log(windowHeight)
    this.setData({
      word:options.word,
      scroll_height:windowHeight-101
    })
    this.getTrans(options.word)
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