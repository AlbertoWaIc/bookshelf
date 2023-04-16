const CheckLoginValidation = function () {
  this.mainValidation = /^[^\s@]+@[^\s@]+\.[^\s@]+$/
  this.minLength = 8
}
CheckLoginValidation.prototype = {
  emailFormat(value) {
    return this.mainValidation.test(value)
  },
  passwordLength(value) {
    if (value.length >= this.minLength) {
      return true
    }
    else {
      return false
    }
  },
  comparePrePassword(value, password) {
    if (value === password) {
      return true
    }
    else {
      return false
    }
  }

}
// export const required = (value) => !!value || 'Required.'
// export const emailFormat = (value) => {
//   const pattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/
//   return pattern.test(value) || 'Invalid email format.'
// }
// export const passwordLength = (value) => value.length >= 8 || 'Password must be at least 8 characters long.'

export const checkLoginValidation = new CheckLoginValidation()