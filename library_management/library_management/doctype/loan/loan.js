// Copyright (c) 2025, Abel Gezahegn and contributors
// For license information, please see license.txt

frappe.ui.form.on("Loan", {
	refresh(frm) {
        frm.add_custom_button(__('Book Now'), function() { alert(frm.doc.type)})
	},
});




// reserve the book
frappe.ui.form.on('Loan', {
    refresh: function(frm) {
        // Add "Book Now" button if status is Available
        if (frm.doc.status === 'Available') {
            frm.add_custom_button(__('Book Now'), function() {
                frappe.confirm(
                    'Are you sure you want to issue this book?',
                    function() {
                        // Update status and issued_to fields
                        frm.set_value('status', 'Issued');
                        frm.set_value('issued_to', frappe.session.user);
                        frm.save();
                    },
                );
            });
        }
    }
});


// return book before deadline
frappe.ui.form.on('Loan', {
    refresh: function(frm) {
        // Add "Return" button if status is Available  and loaned user match with authenticate user 
        if (frm.doc.status === 'Issued' && frm.doc.issued_to === frappe.session.user) {
            frm.add_custom_button(__('Return'), function() {
                frappe.confirm(
                    'Are you sure you want to return this book?',
                    function() {
                        // Update status and issued_to fields
                        frm.set_value('status', 'Available');
                        frm.set_value('issued_to', "");
                        frm.save();
                    },
                );
            });
        }
    }
});



// reissue book 
frappe.ui.form.on('Loan', {
    refresh: function(frm) {
        // Add "Re Issue" button for extends loan day
        if (frm.doc.status === 'Issued' && frm.doc.issued_to === frappe.session.user) {
            frm.add_custom_button(__('Re Issue'), function() {
                frappe.confirm(
                    'Are you sure you want to re issue this book?',
                    function() {
                        // Update status and issued_to fields
                        frm.set_value('status', 'Issued');
                        frm.save();
                    },
                );
            });
        }
    }
});


// set issued to field only visible librarian
frappe.ui.form.on('Book', {
    refresh: function(frm) {
        // Get the current user
        var current_user = frappe.session.user;

        // Check if the current user is the specific user
        if (current_user === 'admin@example.com') {
            // Show the field
            frm.set_df_property('special_field', 'hidden', 0);
        } else {
            // Hide the field
            frm.set_df_property('special_field', 'hidden', 1);
        }
    }
});


