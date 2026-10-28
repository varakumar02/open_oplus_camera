package com.oplus.gallery.aosp;

import android.app.Activity;
import android.app.AlertDialog;
import android.app.WallpaperManager;
import android.content.DialogInterface;
import android.net.Uri;
import android.util.Log;
import android.widget.Toast;

import java.io.InputStream;

/** "Set as wallpaper" asks home, lock or both, then sets the picked image itself (no cropper). */
public final class AospWallpaper implements DialogInterface.OnClickListener {

    private final Activity mActivity;
    private final Uri mUri;

    private AospWallpaper(Activity activity, Uri uri) {
        mActivity = activity;
        mUri = uri;
    }

    public static void show(Activity activity, Uri uri) {
        new AlertDialog.Builder(activity)
                .setTitle("Set wallpaper")
                .setItems(new CharSequence[] {"Home screen", "Lock screen", "Home and lock screens"},
                        new AospWallpaper(activity, uri))
                .show();
    }

    @Override
    public void onClick(DialogInterface dialog, int which) {
        // 0, 1, 2 -> FLAG_SYSTEM, FLAG_LOCK, both
        int flags = which + 1;
        try {
            InputStream in = mActivity.getContentResolver().openInputStream(mUri);
            WallpaperManager.getInstance(mActivity).setStream(in, null, true, flags);
            in.close();
            Toast.makeText(mActivity, "Wallpaper set", Toast.LENGTH_SHORT).show();
        } catch (Exception e) {
            Log.w("AospWallpaper", "setStream failed", e);
        }
    }
}
