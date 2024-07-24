import XCTest

final class marchupTests: XCTestCase {
    let signUpEmail = "INSERT EMAIL FOR SIGN UP TEST HERE(marchup-test)"
    let OTP = "INSERT OTP FOR SIGN UP TEST HERE -- current mm/dd/yy in 123456 format"
    var loginEmail = "INSERT EXISTING ACCOUNT EMAIL HERE"
    var loginPassword = "INSERT EXISTING ACCOUNT PASSWORD HERE"
    let app = XCUIApplication(bundleIdentifier: "com.marchup")
    static var swizzledOutIdle = false
    override func setUpWithError() throws {
        if !marchupTests.swizzledOutIdle {
            // Ensure the swizzle only happens once
            let originalSelector = NSSelectorFromString("waitForQuiescenceIncludingAnimationsIdle:")
            let originalMethod = class_getInstanceMethod((objc_getClass("XCUIApplicationProcess") as! AnyClass), originalSelector)
            let swizzledMethod = class_getInstanceMethod(marchupTests.self, #selector(replace))
            method_exchangeImplementations(originalMethod!, swizzledMethod!)
            marchupTests.swizzledOutIdle = true
        }
        
        try super.setUpWithError()
        continueAfterFailure = false
        app.activate()
        XCTAssertTrue(app.state == .runningForeground, "App did not launch correctly.")
    }
    
    @objc func replace() {
        return
    }
    override func tearDownWithError() throws {
        app.terminate()
    }
    func test1Login() throws {
        let usernameField = app.textFields.element(boundBy: 0)
        let passwordField = app.secureTextFields.element(boundBy: 0)
        let loginButton = app.buttons["Login"]
        
        guard usernameField.waitForExistence(timeout: 5) else {
            throw testError.elementNotFound(description: "Username text field not found")
        }
        guard passwordField.waitForExistence(timeout: 5) else {
            throw testError.elementNotFound(description: "Password text field not found")
        }
        guard loginButton.waitForExistence(timeout: 5) else {
            throw testError.elementNotFound(description: "Login button not found")
        }
        
        usernameField.tap()
        usernameField.typeText(loginEmail)
        
        passwordField.tap()
        passwordField.typeText(loginPassword)
        
        loginButton.tap()
        
        let successMessage = app.textFields.element(boundBy: 0)
        XCTAssertTrue(successMessage.waitForExistence(timeout: 5), "Login failed")
    }
    func test2Logout() throws{
        let settingsButton=app.buttons["Menu, tab, 5 of 5"]
        
        let logoutButton=app.buttons["Logout"]
        
        guard settingsButton.waitForExistence(timeout: 5) else {
            throw testError.elementNotFound(description: "Settings tab button not found")
        }
        settingsButton.tap()
        guard logoutButton.waitForExistence(timeout: 5) else {
            throw testError.elementNotFound(description: "Logout button not found")
        }
        logoutButton.tap()
        let usernameField = app.textFields.element(boundBy: 0)
        XCTAssertTrue(usernameField.waitForExistence(timeout: 5), "Logout not confirmed")
    }

    func test3SignupWithEmail() throws{
        
        let predicate = NSPredicate(format: "label == 'Sign Up Now' AND elementType != %d")
        let signUpElement = app.descendants(matching: .any).matching(predicate).firstMatch
        guard signUpElement.waitForExistence(timeout: 5) else {
            throw testError.elementNotFound(description: "Sign up button not found")
        }
        signUpElement.tap()
        
        let textField = app.textFields.element(boundBy: 0)
        guard textField.waitForExistence(timeout: 5) else {
            throw testError.elementNotFound(description: "Text Field not found")
        }
        textField.tap()
        textField.typeText(signUpEmail)
        
        let createButton = app.buttons["Create Account"]
        guard createButton.waitForExistence(timeout: 5) else {
            throw testError.elementNotFound(description: "CreateButton not found")
        }
        createButton.tap()
        
        
        app.typeText(OTP)
        
        let usernameField = app.textFields.element(boundBy: 0)
        guard usernameField.waitForExistence(timeout: 5) else {
            throw testError.elementNotFound(description: "Username field not found")
        }
        usernameField.tap()
        usernameField.typeText("usernameTest")
        
        let firstName = app.textFields.element(boundBy: 1)
        guard firstName.waitForExistence(timeout: 5) else {
            throw testError.elementNotFound(description: "First Name field not found")
        }
        firstName.tap()
        firstName.typeText("John")
        
        let lastName = app.textFields.element(boundBy: 2)
        guard lastName.waitForExistence(timeout: 5) else {
            throw testError.elementNotFound(description: "Last Name field not found")
        }
        lastName.tap()
        lastName.typeText("Doe")
        
        let passwordField = app.secureTextFields.element(boundBy: 0)
        guard passwordField.waitForExistence(timeout: 5) else {
            throw testError.elementNotFound(description: "Password field not found")
        }
        passwordField.tap()
        passwordField.typeText("password")
        
        let matchPass = app.secureTextFields.element(boundBy: 1)
        guard matchPass.waitForExistence(timeout: 5) else {
            throw testError.elementNotFound(description: "Password matching not found")
        }
        matchPass.tap()
        matchPass.typeText("password")
        
        let nextButton = app.buttons["Next"]
        guard nextButton.waitForExistence(timeout: 5) else {
            throw testError.elementNotFound(description: "Next button not found")
        }
        nextButton.tap()
        
        loginEmail=signUpEmail
        loginPassword="password"
        try test1Login()
        
        let relationshipDrop = app.otherElements["Select Relationship "]
        guard relationshipDrop.waitForExistence(timeout: 5) else {
            throw testError.elementNotFound(description: "Relationship Drop Down button not found")
        }
        relationshipDrop.tap()
        
        let pickerWheel = app.pickerWheels.element
        guard pickerWheel.waitForExistence(timeout: 5) else {
            throw testError.elementNotFound(description: "Picker wheel not found")
        }
        let startPoint = pickerWheel.coordinate(withNormalizedOffset: CGVector(dx: 0.5, dy: 0.8))
        let endPoint = pickerWheel.coordinate(withNormalizedOffset: CGVector(dx: 0.5, dy: 0.2))
        startPoint.press(forDuration: 0.02, thenDragTo: endPoint)
        
        let confirmButton = app.buttons["Confirm"]
        guard confirmButton.waitForExistence(timeout: 5) else {
            throw testError.elementNotFound(description: "Student Choice button not found")
        }
        confirmButton.tap()
        
        nextButton.tap()
        
        let settingsButton=app.buttons["Menu, tab, 5 of 5"]
        guard settingsButton.waitForExistence(timeout: 5) else {
            throw testError.elementNotFound(description: "Settings tab button not found")
        }
        settingsButton.tap()
        
        let deleteAccount=app.buttons["Delete Account"]
        guard deleteAccount.waitForExistence(timeout: 5) else {
            throw testError.elementNotFound(description: "Delete Account button not found")
        }
        deleteAccount.tap()

        app.typeText(OTP)
        let okButton=app.buttons["OK"]
        guard okButton.waitForExistence(timeout: 5) else {
            throw testError.elementNotFound(description: "OK button not found")
        }
        okButton.tap()
        
        sleep(3)
    }
    enum testError: Error {
        case elementNotFound(description: String)
        case unexpectedState(description: String)
    }
}

