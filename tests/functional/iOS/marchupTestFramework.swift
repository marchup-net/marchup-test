import XCTest

final class marchupTests: XCTestCase {
    
    let app = XCUIApplication(bundleIdentifier: "com.marchup")
    //deals with the waiting for app to idle error
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
    let username = "INSERT_USERNAME"
    let password = "INSERT_PASSWORD"
    func testLogin() throws {
        let usernameField = app.textFields.element(boundBy: 0)
        let passwordField = app.secureTextFields.element(boundBy: 0)
        let loginButton = app.buttons["Login"]
        
        guard usernameField.waitForExistence(timeout: 5) else {
            throw LoginoutError.elementNotFound(description: "Username text field not found")
        }
        guard passwordField.waitForExistence(timeout: 5) else {
            throw LoginoutError.elementNotFound(description: "Password text field not found")
        }
        guard loginButton.waitForExistence(timeout: 5) else {
            throw LoginoutError.elementNotFound(description: "Login button not found")
        }
        
        usernameField.tap()
        usernameField.typeText(username)
        
        passwordField.tap()
        passwordField.typeText(password)
        
        loginButton.tap()
        
        let successMessage = app.textFields.element(boundBy: 0)
        XCTAssertTrue(successMessage.waitForExistence(timeout: 5), "Login failed")
    }
    func testLogout() throws{
        let settingsButton=app.buttons["Menu, tab, 5 of 5"]
        
        let logoutButton=app.buttons["Logout"]
        
        guard settingsButton.waitForExistence(timeout: 5) else {
            throw LoginoutError.elementNotFound(description: "Settings tab button not found")
        }
        settingsButton.tap()
        guard logoutButton.waitForExistence(timeout: 5) else {
            throw LoginoutError.elementNotFound(description: "Logout button not found")
        }
        logoutButton.tap()
        let usernameField = app.textFields.element(boundBy: 0)
        XCTAssertTrue(usernameField.waitForExistence(timeout: 5), "Logout not confirmed")
    }
        enum LoginoutError: Error {
            case elementNotFound(description: String)
            case unexpectedState(description: String)
        }
    }

