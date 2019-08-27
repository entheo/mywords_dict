//const weui = '/miniprogram_npm/weui-miniprogram'

App({

  onLaunch: function () {
    // 展示本地存储能力
    var logs = wx.getStorageSync('logs') || []
    logs.unshift(Date.now())
    wx.setStorageSync('logs', logs)

    // 登录
    wx.login({
      success: res => {
        // 发送 res.code 到后台换取 openId, sessionKey, unionId
      }
    })
    // 获取用户信息
    wx.getSetting({
      success: res => {
        if (res.authSetting['scope.userInfo']) {
          // 已经授权，可以直接调用 getUserInfo 获取头像昵称，不会弹框
          wx.getUserInfo({
            success: res => {
              // 可以将 res 发送给后台解码出 unionId
              this.globalData.userInfo = res.userInfo

              // 由于 getUserInfo 是网络请求，可能会在 Page.onLoad 之后才返回
              // 所以此处加入 callback 以防止这种情况
              if (this.userInfoReadyCallback) {
                this.userInfoReadyCallback(res)
              }
            }
          })
        }
      }
    })
  },
  
//登录
  signUp: function (callback) {
    wx.login({
      success: res => {
        // 发送 res.code 到后台换取 openId, sessionKey, unionId
        console.log(res)
        wx.request({
          url: this.globalData.host + '/weixin/login/',
          method: 'POST',
          header: {
            'Content-Type': 'application/x-www-form-urlencoded'},
          data: {
            code: res.code,
            hi:'hinihoa'
          },
          success: res => {
            console.log(res.data)
            wx.setStorageSync('token', res.data.token)
            wx.setStorageSync('open_id', res.data.open_id)
            callback()
          },

        })
      }
    })
  },

//校验并获取用户token
  getToken: function () {
    let promise = new Promise((resolv, reject) => {
      if (wx.getStorageSync('token') == '') {
        this.signUp(function () {
          resolv('got token')
        })
      }
      else {
        resolv('got token')
      }
    })
    return promise
  },

  change: function (e) {
    console.log(e)
    var url = e.detail.item.pagePath
    wx.switchTab({
      url:url,
      success: function(res) {
        console.log('success',res)
      },
      fail: function(res) {
        console.log('fail',res)
      },
      complete: function(res) {
        console.log('com',res)
      },
    })
  },

  //全局变量
  globalData: {
    userInfo: null,
    host:'http://10.0.0.4:8080',
    list: [{
        text: "词典",
        pagePath:"../index/index",
        iconPath: "images/dict.png",
        selectedIconPath: "images/dict_activated.png",
      },
      {
        text: "生词本",
        pagePath:"../memo/memo",
        iconPath: "images/memo.png",
        selectedIconPath: "images/memo_activated.png",
        //badge: 'New'
      }]
    },

})